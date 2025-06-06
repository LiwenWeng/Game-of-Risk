from game.events.base_event import Event

class IndustryPartnership(Event):
    name = "Industry Partnership"
    description = "You’ve partnered with a major security firm for infrastructure upgrades."

    def __init__(self, state, player):
        super().__init__(state, player, weight=1)

    def apply(self):
        for defense in self.state.all_defenses:
            defense.effectiveness *= 1.05
        self.state.log("All defenses received a 5% effectiveness boost.")

    def process_weight(self):
        if self.state.current_day % 7 == 0:
            self.weight += 1
