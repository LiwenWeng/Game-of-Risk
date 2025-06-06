from game.defenses.base_defense import Defense
from game import State

class TimedDefense(Defense):
    def __init__(self, cost: int, effectiveness: float, state: State, duration: int):
        super().__init__(cost, effectiveness, state)
        self.duration = duration
        self.remaining_days = duration

    def tick(self):
        if self.active:
            self.remaining_days -= 1
            if self.remaining_days <= 0:
                self.remaining_days = self.duration
                self.deactivate()

    def __str__(self) -> str:
        base = super().__str__()
        if self.active:
            base += f"\nExpires in: {self.remaining_days} day(s)"
        return base