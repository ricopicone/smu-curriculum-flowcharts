def term_sort_key(term):
        """
        Custom sort key for terms in the format 'YYYY-F', 'YYYY-S', etc.
        Converts terms to a tuple of (year, season_order) for sorting.
        """
        import re
        match = re.match(r"(\d+)-([A-Za-z]+)", term)
        if not match:
            return (term,)
        year, season = match.groups()
        season_order = {'S': 0, 'Su': 1, 'Su1': 2, 'Su2': 3, 'F': 4}
        return (int(year), season_order.get(season, 99))

VALID_CATEGORIES = {
        "C": "C", "Core": "C",
        "MS": "MS", "Math and Science": "MS",
        "GE": "GE", "General Engineering": "GE",
        "ME": "ME", "Mechanical Engineering": "ME",
        "O": "O", "Other": "O",
        "F": "F", "Foundation": "F",
        "Con": "Con", "Conversatio": "Con",
        "Ora": "Ora",
    }

def normalize_categories(categories):
    if isinstance(categories, str):
        categories = [categories]
    for cat in categories:
        if cat not in VALID_CATEGORIES:
            raise ValueError(f"Invalid course category: {cat}. Must be one of: {', '.join(VALID_CATEGORIES.keys())}")
    return [VALID_CATEGORIES[c] for c in categories if c in VALID_CATEGORIES]