class Event:
    name = "Generic Event"
    description = "Something happens..."

    def __init__(self, state, player, weight: int = 1):
        self.state = state
        self.player = player
        self.weight = weight

    def proccess_weight(self):
        raise NotImplementedError("Override this in subclasses")

    def apply(self):
        raise NotImplementedError("Override this in subclasses")
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"