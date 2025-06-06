from game.defenses.variants import DependentDefense
from game import State

class SIEM(DependentDefense):
    name = "SIEM"
    description = "Centralized log and event correlation system."

    def __init__(self, state: State):
        super().__init__(
            cost=10000,
            effectiveness=0.5,
            state=state,
            required=["Firewall", "Intrusion Detection System", "Multi-Factor Authentication"]
        )