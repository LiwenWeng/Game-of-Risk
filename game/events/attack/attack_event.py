from game.events.base_event import Event

class AttackEvent(Event):
    name = "Generic Attack"
    description = "Attacked..."

    def __init__(self, state, player, weight, threat_level: float):
        super().__init__(state, player, weight)
        self.threat_level = threat_level