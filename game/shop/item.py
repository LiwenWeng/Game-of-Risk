class Item:
    def __init__(self, name: str, description: str, price: int = 0, effect: str = "", consumable: bool = True):
        self.name = name
        self.description = description
        self.price = price
        self.effect = effect
        self.consumable = consumable

    def __str__(self):
        return f"{self.name} - ${self.price}\n  {self.description}"
    