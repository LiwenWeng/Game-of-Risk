from game.defenses.variants import TimedDefense
from game import State

class Antivirus(TimedDefense):
    name = "Antivirus"
    description = "Detects and removes known malware. Requires regular updates."

    def __init__(self, state: State):
        super().__init__(
            cost=3000,
            effectiveness=0.3,
            state=state,
            duration=3
        )