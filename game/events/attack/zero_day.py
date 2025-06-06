from game.events.attack import AttackEvent

class ZeroDayExploit(AttackEvent):
    name = "Zero-Day Exploit"
    description = "An unknown software vulnerability was exploited."

    def __init__(self, state, player):
        super().__init__(state, player, weight=1, threat_level=0.9)

    def apply(self):
        effective_threat = self.threat_level
        for defense in self.state.active_defenses.values():
            if defense.name == "Antivirus":
                continue
            effective_threat = defense.apply_defense(effective_threat)

        if effective_threat < 0.5:
            self.state.log("AI anomaly detection prevented zero-day escalation.")
        else:
            loss = round(self.state.asset_value * effective_threat * 0.2)
            self.state.asset_value -= loss
            self.state.log(f"Zero-day exploit caused serious compromise. Loss: ${loss:,}.")

    def process_weight(self):
        return self.weight * (1.5 if self.state.current_day >= 5 else 1)
