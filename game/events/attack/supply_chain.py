from game.events.attack import AttackEvent

class SupplyChainBreach(AttackEvent):
    name = "Supply Chain Breach"
    description = "A vendor was compromised, exposing your systems."

    def apply(self):
        effective_threat = self.threat_level
        for defense in self.state.active_defenses.values():
            if defense.name == "SIEM":
                effective_threat *= 0.6
            else:
                effective_threat = defense.apply_defense(effective_threat)

        if effective_threat < 0.4:
            self.state.log("SIEM detected suspicious external behavior early.")
        else:
            loss = round(self.state.asset_value * effective_threat * 0.12)
            self.state.asset_value -= loss
            self.state.log(f"Supply chain attack bypassed basic defenses. Loss: ${loss:,}.")

    def process_weight(self):
        return self.weight * (1.3 if self.state.current_day > 3 else 1)
