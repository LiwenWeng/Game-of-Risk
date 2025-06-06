from game.defenses.variants import DependentDefense
from game import State

class AIAnomalyDetection(DependentDefense):
    name = "AI Anomaly Detection"
    description = "Uses AI to detect unknown threats. Requires supporting infrastructure."

    def __init__(self, state: State):
        super().__init__(
            cost=8000,
            effectiveness=0.6,
            state=state,
            required=["Firewall", "Intrusion Detection System"]
        )