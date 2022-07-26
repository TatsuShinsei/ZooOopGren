from .item import Item


class MagnifyingGlass(Item):
    def __init__(self, name, description, weight):
        super().__init__(name, description, weight)

    def use(self):
        print(f"you just used {self.name}")
        input()
