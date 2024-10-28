class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=0):
        """Function class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string"""
        return f"{self.name}, {self.typing} typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if dynamic or not"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
