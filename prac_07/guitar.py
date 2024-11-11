CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """Class for storing data"""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Function for returning string representation of a guitar"""
        return f"{self.name} ({self.year} : ${self.cost:,.2f} )"

    def get_age(self):
        """Function for getting the age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Function to determine whether the guitar is vintage or not """
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """Less-than comparison based on the year attribute"""
        return self.year < other.year
