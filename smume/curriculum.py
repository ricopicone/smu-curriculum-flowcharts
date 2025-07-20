from smume.course_model import Course

class Curriculum:
    """
    Container for a curriculum's set of courses. Defines structure, not term plans.
    """

    def __init__(self, name: str):
        self.name = name
        self.courses = {}

    def course(self, name, credits, **kwargs):
        """
        Creates and registers a course in the curriculum.
        Does not set term or completion status.
        """
        course = Course(name, credits, **kwargs)
        self.courses[name] = course
        return course
