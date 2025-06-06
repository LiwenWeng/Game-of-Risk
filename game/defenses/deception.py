from game.defenses.variants import TimedDefense
from game import State

class DeceptionTechnology(TimedDefense):
    name = "Deception Technology"
    description = "Deploys fake systems to trap attackers and delay real damage."

    def __init__(self, state: State):
        super().__init__(
            cost=12000,
            effectiveness=0.3,
            state=state,
            duration=3
        )