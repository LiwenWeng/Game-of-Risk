from game.events.base_event import Event

class GrantAIDevelopment(Event):
    name = "Grant for AI Development"
    description = "A government agency funds your AI anomaly detection improvements."

    def __init__(self, state, player):
        super().__init__(state, player, weight=1)

    def apply(self):
        self.state.free_defense_activations.add("AI Anomaly Detection")
        self.state.log("AI Anomaly Detection is free to activate today!")

    def process_weight(self):
        if not self.state.is_defense_active("AI Anomaly Detection"):
            self.weight += 1
