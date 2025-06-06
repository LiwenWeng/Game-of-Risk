from game.events.base_event import Event

class InvestorConfidence(Event):
    name = "Investor Confidence Surge"
    description = "A glowing cybersecurity audit impresses investors."

    def __init__(self, state, player):
        super().__init__(state, player, weight=2)

    def apply(self):
        gain = round(self.player.asset_value * 0.15)
        self.player.asset_value += gain
        self.state.log(f"Investor confidence boosted assets by ${gain:,}.")

    def process_weight(self):
        if self.state.risk_level < 0.5:
            self.weight += 2