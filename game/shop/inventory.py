class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str, quantity: int = 1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int = 1) -> bool:
        if self.items.get(item_name, 0) >= quantity:
            self.items[item_name] -= quantity
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True

        return False
    
    def has_item(self, item_name: str, quantity: int = 1) -> bool:
        return self.items.get(item_name, 0) >= quantity

    def get_items(self) -> dict:
        return dict(self.items)
    
    def print_inventory(self):
        if not self.items:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for name, qty in self.items.items():
                print(f" - {name}: {qty}")