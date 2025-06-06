class Player():
    def __init__(self, starting_budget: int = 15000):
        self.name = ""
        self.budget = starting_budget
        
    def set_name(self, name: str):
        self.name = name

