from game.events.base_event import Event

class DataMisconfiguration(Event):
    name = "Data Misconfiguration"
    description = "A team accidentally exposes sensitive data during maintenance."

    def __init__(self, state, player):
        super().__init__(state, player, weight=2)

    def apply(self):
        if not self.state.is_defense_active("Network Segmentation"):
            self.state.risk_level += 0.15
            self.state.log("Data leak increased risk due to lack of segmentation.")
        else:
            self.state.log("Network Segmentation mitigated a misconfiguration risk.")

    def process_weight(self):
        if not self.state.is_defense_active("Network Segmentation"):
            self.weight += 2