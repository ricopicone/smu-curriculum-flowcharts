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