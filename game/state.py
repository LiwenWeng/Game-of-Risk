from colorama import Fore, Style
from game.utils.display import colored_text, print_colored, type_text

class State:
    def __init__(self, max_days: int = 30, starting_asset_value: int = 100_000):
        self.max_days = max_days
        self.current_day = 1
        self.is_over = False
        self.win = False

        self.risk_level = 0
        self.logs: dict[int, list] = {}

        self.asset_value = starting_asset_value
        self.asset_growth_rate = 1.01
        self.active_defenses = {}
        self.defense_activation_locked = False
    
    def change_asset_value(self, amount: int):
        self.asset_value += amount
        action = "gained" if amount > 0 else "lost"
        self.log(f"Company {action} ${abs(amount):,}. New value: ${self.asset_value:,}")

        if self.asset_value <= 0:
            self.end_game(win=False, reason="Company went bankrupt.")

    def is_defense_active(self, defense_name: str) -> bool:
        return defense_name in self.active_defenses

    def log(self, message: str):
        if not self.logs.get(self.current_day):
            self.logs[self.current_day] = []
        
        self.logs[self.current_day].append(message)

    def view_logs(self, day: int):
        if day not in self.logs or not self.logs[day]:
            print_colored(f"No logs found for Day {day}.", Fore.YELLOW)
            return

        print_colored(f"Logs for Day {day}\n", Fore.MAGENTA, Style.BRIGHT)

        for entry in self.logs[day]:
            type_text(colored_text("- " + entry, Fore.WHITE), 0.01)

    def advance_day(self):
        self.update_assets()
        self.current_day += 1
        if self.current_day > self.max_days:
            self.end_game(win=True, reason=f"Lasted {self.max_days}")

    def update_assets(self):
        self.asset_value = round(self.asset_value * self.asset_growth_rate)
    
    def end_game(self, win: bool, reason: str = ""):
        self.is_over = True
        self.win = win
        self.log("Game Over: " + ("You won!" if win else "You lost."))
        if reason:
            self.log("Reason: " + reason)
    
    def reset(self):
        self.__init__(self.max_days, self.asset_value)
    