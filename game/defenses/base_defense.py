from colorama import Fore
from game import State
from game.utils import colored_text

class Defense:
    name = "Generic Defense"
    description = "Defend against..."

    def __init__(self, cost: int, effectiveness: float, state: State):
        self.cost = cost
        self.effectiveness = effectiveness
        self.active = False
        self.state = state

    def __str__(self) -> str:
        status = colored_text("Active", Fore.GREEN) if self.active else colored_text("Inactive", Fore.RED)
        return (f"{self.name} ({status})\n"
                f"Effectiveness: {self.effectiveness * 100:.0f}%\n"
                f"Cost: ${self.cost:,}\n"
                f"{self.description}")

    def activate(self) -> bool:
        if self.active: 
            return False
        
        self.active = True
        self.state.active_defenses[self.name] = self
        self.state.log(f"Purchased for ${self.cost:,} and activated defense: {self.name}.")

        return True

    def deactivate(self):
        if not self.active:
            return
        
        self.active = False
        self.state.active_defenses.pop(self.name, None)
        self.state.log(f"{self.name} was deactivated.")

    def apply_defense(self, threat_level: float) -> float:
        if self.active:
            return threat_level * (1 - self.effectiveness)
        return threat_level
    