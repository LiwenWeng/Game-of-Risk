from game.events.attack import AttackEvent

class DDOS(AttackEvent):
    name = "DDoS Attack"
    description = "A large-scale DDoS attack disrupted services."

    def __init__(self, state, player):
        super().__init__(state, player, weight=1, threat_level=0.5)

    def apply(self):
        effective_threat = self.threat_level
        for defense in self.state.active_defenses.values():
            if "Firewall" in defense.name:
                effective_threat *= 0.7
            else:
                effective_threat = defense.apply_defense(effective_threat)

        if effective_threat < 0.5:
            self.state.log("Firewall mitigated most of the DDoS attack.")
        else:
            self.state.log("DDoS attack caused major slowdowns and service outages.")

    def process_weight(self):
        return self.weight * (0.8 if "Firewall" in self.state.active_defenses else 1.2)