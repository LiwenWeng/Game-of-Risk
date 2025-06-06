from game.defenses import Antivirus
from game.events.attack import AttackEvent

class Ransomware(AttackEvent):
    name = "Ransomware Attack"
    description = "Critical systems have been locked, demanding a ransom."

    def apply(self):
        effective_threat = self.threat_level
        for defense in self.state.active_defenses.values():
            if isinstance(defense, Antivirus):
                continue
            effective_threat = defense.apply_defense(effective_threat)

        if effective_threat < 0.5:
            self.state.log("Ransomware was contained by proactive defenses.")
        else:
            loss = round(self.state.asset_value * effective_threat * 0.1)
            self.state.asset_value -= loss
            self.state.log(f"Paid ransom to regain access. Asset loss: ${loss:,}.")

    def process_weight(self):
        return self.weight * (1.25 if "Antivirus" not in self.state.active_defenses else 1.0)