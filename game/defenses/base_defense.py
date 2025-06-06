from game import State

class Defense:
    name = "Generic Defense"
    description = "Defend against..."

    def __init__(self, cost: int, effectiveness: float, state: State):
        self.cost = cost
        self.effectiveness = effectiveness
        self.active = False
        self.state = state

    def __str__(self) -> str:
        status = "Active" if self.active else "Inactive"
        return (f"{self.name} ({status})\n"
                f"Effectiveness: {self.effectiveness * 100:.0f}%\n"
                f"Cost: ${self.cost:,}\n"
                f"{self.description}")

    def activate(self):
        if self.active: 
            return
        
        self.active = True
        self.state.active_defenses[self.name] = self

    def deactivate(self):
        if not self.active:
            return
        
        self.active = False
        self.state.active_defenses.pop(self.name, None)

    def apply_defense(self, threat_level: float) -> float:
        if self.active:
            return threat_level * (1 - self.effectiveness)
        return threat_level
    