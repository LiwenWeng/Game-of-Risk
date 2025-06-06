from game.events.attack.attack_event import AttackEvent

class InsiderThreat(AttackEvent):
    name = "Insider Threat"
    description = "An employee with access leaked or sabotaged sensitive systems."

    def __init__(self, state, player):
        super().__init__(state, player, weight=1, threat_level=0.7)

    def apply(self):
        effective_threat = self.threat_level
        for defense in self.state.active_defenses.values():
            if defense.name == "Deception Technology":
                effective_threat *= 0.5
            else:
                effective_threat = defense.apply_defense(effective_threat)

        if effective_threat < 0.5:
            self.state.log("Insider threat contained through internal monitoring.")
        else:
            loss = round(self.state.asset_value * effective_threat * 0.15)
            self.state.change_asset_value(-loss)
            self.state.risk_level = min(1.0, self.state.risk_level + 0.07)
            self.state.log(f"Insider leaked data. Assets impacted by ${loss:,}.")

    def process_weight(self):
        return self.weight * (1.3 if self.state.asset_value > 750_000 else 1)
