from game.events.base_event import Event

class BudgetCuts(Event):
    name = "Budget Cuts"
    description = "CFO mandates a temporary freeze on all upgrades."

    def apply(self):
        self.state.defense_activation_locked = True
        self.state.log("New defense activations are disabled for the day due to budget cuts.")

    def process_weight(self):
        if self.player.asset_value > 100_000:
            self.weight += 1
