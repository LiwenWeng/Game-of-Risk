from game.defenses.base_defense import Defense
from game import State

class DiminishingDefense(Defense):
    def __init__(self, cost: int, effectiveness: float, state: State, decay_rate: float = 0.05):
        super().__init__(cost, effectiveness, state)
        self.decay_rate = decay_rate

    def apply_defense(self, threat_level: float) -> float:
        if self.active:
            reduced_threat = threat_level * (1 - self.effectiveness)
            self.effectiveness = max(0, self.effectiveness - self.decay_rate)
            return reduced_threat
        return threat_level
