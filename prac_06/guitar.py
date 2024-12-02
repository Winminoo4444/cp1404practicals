CURRENT_TIME = 2024


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Function for the classes"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string"""
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """Function to calculate age"""
        age = CURRENT_TIME - self.year
        return age

    def is_vintage(self):
        """Check if the guitar is vintage or not"""
        age = self.get_age()
        if age > 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """Comparing two guitar instances"""
        return self.year < other.year
