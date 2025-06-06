from typing import Iterable
from colorama import Fore

from game.defenses.base_defense import Defense
from game import State
from game.utils import print_colored

class DependentDefense(Defense):
    def __init__(self, cost: int, effectiveness: float, state: State, required: Iterable[str]):
        super().__init__(cost, effectiveness, state)
        self.required = list(required)

    def can_activate(self) -> bool:
        return all(req in self.state.active_defenses for req in self.required)

    def activate(self) -> bool:
        if not self.can_activate():
            missing = [r for r in self.required if r not in self.state.active_defenses]
            print_colored(f"{self.name} cannot be activated. Missing: {', '.join(missing)}", Fore.RED)
            return False
        super().activate()

    def __str__(self) -> str:
        base = super().__str__()
        requirements = ", ".join(self.required)
        return base + f"\nRequires: {requirements}"