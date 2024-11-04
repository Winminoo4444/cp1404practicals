class Project:
    def __init__(self, name, start_date, priority=0, cost_estimate=0.0, completion_percentage=0):
        """Function to construct from the given values."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Function for returning string representation"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}% "

    def __repr__(self):
        """Funciton for returning string representation"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}," \
               f" estimate: ${self.cost_estimate}, completion: {self.completion_percentage}% "

    def __lt__(self, other):
        """Function to sort the list of projects based on priority number."""
        return self.priority < other.priority
