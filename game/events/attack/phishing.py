from game.events.attack import AttackEvent

class Phishing(AttackEvent):
    name = "Phishing Scam"
    description = "Employees received deceptive emails leading to data compromise."

    def __init__(self, state, player):
        super().__init__(state, player, weight=2, threat_level=0.6)

    def apply(self):
        effective_threat = self.threat_level
        for defense in self.state.active_defenses.values():
            effective_threat = defense.apply_defense(effective_threat)

        if "Multi-Factor Authentication" in self.state.active_defenses:
            effective_threat *= 0.6

        if effective_threat < 0.4:
            self.state.log("MFA and training mitigated the phishing campaign.")
        else:
            loss = round(self.state.asset_value * effective_threat * 0.08)
            self.state.change_asset_value(-loss)
            self.state.risk_level = min(1.0, self.state.risk_level + 0.05)
            self.state.log(f"Phishing scam compromised accounts. Loss: ${loss:,}.")

    def process_weight(self):
        return self.weight * (1.5 if self.state.asset_value > 1_000_000 else 1)
