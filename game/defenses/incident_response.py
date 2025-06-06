from game.defenses.variants import TimedDefense
from game import State

class IncidentResponsePlan(TimedDefense):
    name = "Incident Response Plan"
    description = "Preparedness strategy that reduces damage in case of an incident."

    def __init__(self, state: State):
        super().__init__(
            cost=4500,
            effectiveness=0.4,
            state=state,
            duration=2
        )