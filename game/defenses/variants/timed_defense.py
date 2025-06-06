from game.defenses.base_defense import Defense
from game import State

class TimedDefense(Defense):
    def __init__(self, cost: int, effectiveness: float, state: State, duration: int):
        super().__init__(cost, effectiveness, state)
        self.duration = duration
        self.remaining_days = duration

    def on_day_start(self):
        if self.active:
            self.remaining_days -= 1
            if self.remaining_days <= 0:
                self.deactivate()

    def get_summary(self) -> str:
        base = super().get_summary()
        if self.active:
            base += f"\nExpires in: {self.remaining_days} day(s)"
        return base