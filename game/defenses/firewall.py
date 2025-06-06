from game.defenses.variants import DiminishingDefense
from game import State

class Firewall(DiminishingDefense):
    name = "Firewall"
    description = "Protects your network perimeter, but becomes outdated over time."

    def __init__(self, state: State):
        super().__init__(
            cost=4000,
            effectiveness=0.4,
            state=state,
            decay_rate=0.05
        )