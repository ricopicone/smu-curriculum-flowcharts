import re
from smume.utils import term_sort_key

def catalog_to_module_name(catalog):
    """
    Normalize a human-friendly catalog string to a valid Python module name.
    Examples:
        "ME 2024–25" -> "_2024_25"
        "2024–25"    -> "_2024_25"
        "2024-2025"  -> "_2024_25"
    """
    match = re.search(r"(\d{4})\D+(\d{2,4})", catalog)
    if match:
        start_year, end_year = match.groups()
        end_year = end_year[-2:]  # get last 2 digits
        return f"_{start_year}_{end_year}"
    raise ValueError(f"Unrecognized catalog format: {catalog}")


import importlib

class GenericPlan:
    """
    A plan representing the default recommended sequence for a given catalog year.
    Stores the initial term layout as defined in the curriculum module.
    """

    def __init__(self, catalog):
        self.course_terms = {}

        if isinstance(catalog, str):
            module_name = catalog_to_module_name(catalog)
            mod = importlib.import_module(f"smume.curricula.{module_name}")
            self.curriculum = mod.curriculum
            self.catalog = catalog
        else:
            self.curriculum = catalog
            self.catalog = str(catalog)

        self.course_terms = {
            name: course.term for name, course in self.curriculum.courses.items()
        }

    @property
    def courses(self):
        return self.curriculum.courses.values()

    def get_term(self, course_name):
        return self.course_terms.get(course_name)

    def set_term(self, course_name, term):
        if course_name in self.course_terms:
            self.course_terms[course_name] = term
            if course_name in self.curriculum.courses:
                self.curriculum.courses[course_name].term = term

    def apply_term_mapping(self, term_map: dict, check: bool = False):
        """
        Updates course terms based on a dictionary like:
        {
            "1F": ["ME 345", "ME 316"],
            "1S": ["ME 392"]
        }
        Only updates terms for the listed courses. Other courses remain unchanged.
        If check=True, returns a dictionary of dependency issues.
        """
        for term, course_list in term_map.items():
            for course_name in course_list:
                self.set_term(course_name, term)

        if check:
            return self.check_dependencies()
    
    def courses_by_term(self):
        grouped = {}
        for course in self.courses:
            grouped.setdefault(course.term, []).append(course)
        return grouped

    def check_dependencies(self):
        """
        Check for unmet prerequisites, corequisites, and coprerequisites
        in the course plan. Returns a dictionary of problems keyed by course name.
        """
        problems = {}

        term_order = sorted(
            {t for t in self.course_terms.values() if t is not None},
            key=term_sort_key
        )
    
        term_index = {term: i for i, term in enumerate(term_order)}

        for course in self.courses:
            course_term = self.course_terms.get(course.name)
            course_index = term_index.get(course_term, -1)

            unmet = {"prereq": [], "coreq": [], "coprereq": []}

            for pre in getattr(course, "prereqs", []):
                pre_term = self.course_terms.get(pre)
                if pre_term is None or term_index.get(pre_term, -1) >= course_index:
                    unmet["prereq"].append(pre)

            for co in getattr(course, "coreqs", []):
                co_term = self.course_terms.get(co)
                if co_term is None or term_index.get(co_term, -1) != course_index:
                    unmet["coreq"].append(co)

            for copre in getattr(course, "coprereqs", []):
                copre_term = self.course_terms.get(copre)
                if copre_term is None or term_index.get(copre_term, -1) > course_index:
                    unmet["coprereq"].append(copre)

            if any(unmet.values()):
                problems[course.name] = unmet

        return problems
    
    def print_dependency_issues(self):
        """
        Print any unmet prerequisites, corequisites, or coprerequisites.
        """
        issues = self.check_dependencies()
        if not issues:
            print("No dependency issues found.")
            return

        for course_name, unmet in issues.items():
            print(f"Course: {course_name}")
            if unmet["prereq"]:
                print(f"  Unmet Prerequisites: {', '.join(unmet['prereq'])}")
            if unmet["coreq"]:
                print(f"  Unmet Corequisites: {', '.join(unmet['coreq'])}")
            if unmet["coprereq"]:
                print(f"  Unmet Coprerequisites: {', '.join(unmet['coprereq'])}")