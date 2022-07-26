from .item import Item


class Key(Item):
    def __init__(self, name, description, weight, level: int):
        super().__init__(name, description, weight)
        self.level = level

    def use(self):
        print(f"you just used {self.name}")
        input()
