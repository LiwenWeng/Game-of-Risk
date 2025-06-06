from game.defenses.base_defense import Defense
from game import State

class MultiFactorAuthentication(Defense):
    name = "Multi-Factor Authentication"
    description = "Hardens access control by requiring a second authentication method."

    def __init__(self, state: State):
        super().__init__(
            cost=5500,
            effectiveness=0.2,
            state=state
        )