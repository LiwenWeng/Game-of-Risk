from game.defenses.variants import DiminishingDefense
from game import State

class IntrusionDetectionSystem(DiminishingDefense):
    name = "Intrusion Detection System"
    description = "Monitors traffic for suspicious activity. Gets less effective without tuning."

    def __init__(self, state: State):
        super().__init__(
            cost=6500,
            effectiveness=0.5,
            state=state,
            decay_rate=0.1
        )