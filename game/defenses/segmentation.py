from game.defenses.base_defense import Defense
from game import State

class NetworkSegmentation(Defense):
    name = "Network Segmentation"
    description = "Divides your network to prevent full-system breaches."

    def __init__(self, state: State):
        super().__init__(
            cost=7500,
            effectiveness=0.25,
            state=state
        )