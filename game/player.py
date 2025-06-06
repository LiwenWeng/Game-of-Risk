class Player():
    def __init__(self, starting_budget: int = 15000):
        self.name = ""
        self.budget = starting_budget
        self.pay_rate = 0.01
        
    def set_name(self, name: str):
        self.name = name

    def recieve_paycheck(self, asset_value: int):
        self.budget += round(asset_value * self.pay_rate)