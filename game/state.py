class State:
    def __init__(self, max_days: int = 30, starting_asset_value: int = 100_000):
        self.max_days = max_days
        self.current_day = 1
        self.is_over = False
        self.win = False

        self.risk_level = 0
        self.logs = []

        self.asset_value = starting_asset_value
    
    def change_asset_value(self, amount: int):
        self.asset_value += amount
        action = "gained" if amount > 0 else "lost"
        self.log(f"Company {action} ${abs(amount):,}. New value: ${self.asset_value:,}")

        if self.asset_value <= 0:
            self.end_game(win=False, reason="Company went bankrupt.")

    def log(self, message: str):
        self.logs.append(f"Day {self.current_day}: {message}")

    def advance_day(self):
        self.current_day += 1
        if self.current_day > self.max_days:
            self.end_game(win=True, reason=f"Lasted {self.max_days}")
    
    def end_game(self, win: bool, reason: str = ""):
        self.is_over = True
        self.win = win
        self.log("Game Over: " + ("You won!" if win else "You lost."))
        if reason:
            self.log("Reason: " + reason)
    
    def reset(self):
        self.__init__(self.max_days, self.asset_value)
    