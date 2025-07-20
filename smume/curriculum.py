from smume.course_model import Course

class Curriculum:
    """
    Container for a curriculum's set of courses. Defines structure, not term plans.
    """

    def __init__(self, name: str):
        self.name = name
        self.courses = {}
        self.category_requirements = {}

    def course(self, name, credits, **kwargs):
        """
        Creates and registers a course in the curriculum.
        Does not set term or completion status.
        """
        course = Course(name, credits, **kwargs)
        self.courses[name] = course
        return course

    def category_requirement(self, category: str, kind: str, number: int = None, note: str = None):
        """
        Defines a category requirement for the curriculum.
        """
        if category not in self.category_requirements:
            self.category_requirements[category] = []
        self.category_requirements[category].append({
            "kind": kind,
            "number": number,
            "note": note
        })
        return self
