from game.events.base_event import Event

class BudgetCuts(Event):
    name = "Budget Cuts"
    description = "CFO mandates a temporary freeze on all upgrades."

    def __init__(self, state, player):
        super().__init__(state, player, weight=1)

    def apply(self):
        self.state.defense_activation_locked = True
        self.state.log("New defense activations are disabled for the day due to budget cuts.")

    def process_weight(self):
        if self.state.asset_value > 100_000:
            self.weight += 1
