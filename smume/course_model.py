# course_model.py

class Course:
    """Defines a course with relationships and metadata."""

    VALID_CATEGORIES = {
        "C": "C", "Core": "C",
        "MS": "MS", "Math and Science": "MS",
        "GE": "GE", "General Engineering": "GE",
        "ME": "ME", "Mechanical Engineering": "ME",
        "O": "O", "Other": "O"
    }

    def __init__(self, name, credits, term=None, completed=False, category=None, full_name=None, note=None):
        self.name = name
        self.credits = credits
        self.term = term
        self.completed = completed
        self.prereqs = []
        self.coreqs = []
        self.coprereqs = []
        self.styles = {}
        self.category = self._normalize_category(category)
        self.full_name = full_name or name
        self.note = note
        if self.note is None:
            if self.full_name:
                self.note = f"{self.full_name}"
            else:
                self.note = f"{self.name} ({self.credits} cr)"

    def _normalize_category(self, category):
        if category is None:
            return None
        normalized = self.VALID_CATEGORIES.get(category)
        if not normalized:
            raise ValueError(f"Invalid course category: {category}. Must be one of: {', '.join(self.VALID_CATEGORIES.keys())}")
        return normalized

    def add_prereq(self, prereq_name):
        self.prereqs.append(prereq_name)
        return self

    def add_coreq(self, coreq_name):
        self.coreqs.append(coreq_name)
        return self

    def add_coprereq(self, coprereq_name):
        self.coprereqs.append(coprereq_name)
        return self

    def add_style(self, style_key, style_value):
        self.styles[style_key] = style_value
        return self

    def set_completed(self, completed=True):
        self.completed = completed
        return self

def new_course(name, credits, term=None, completed=False, category=None):
    """Creates and registers a new course."""
    course = Course(name, credits, term, completed, category)
    return course