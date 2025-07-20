import re

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

    def apply_term_mapping(self, term_map: dict):
        """
        Updates course terms based on a dictionary like:
        {
            "1F": ["ME 345", "ME 316"],
            "1S": ["ME 392"]
        }
        Only updates terms for the listed courses. Other courses remain unchanged.
        """
        for term, course_list in term_map.items():
            for course_name in course_list:
                self.set_term(course_name, term)
    
    def courses_by_term(self):
        grouped = {}
        for course in self.courses:
            grouped.setdefault(course.term, []).append(course)
        return grouped