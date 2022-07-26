class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class MaxSoltsExeption(Exception):
    def __init__(self, message="Maxximun ammount of items raeached, douldn't add the item to the inventory"):
        self.message = message
        super().__init__(self.message)


class Bag(metaclass=NamedMeta):
    def __init__(self, items: list):
        self.items = items
        self.maxslots = 10
        self.usedslots = int()
        self.add_items(items)

    def add_items(self, arg):
        if isinstance(arg, list):
            for i in arg:
                if self.usedslots + i.weight > self.maxslots:
                    raise MaxSoltsExeption()
                self.items.append(i)
                self.usedslots += i.weight
        else:
            if self.usedslots + arg.weight > self.maxslots:
                raise MaxSoltsExeption()
            self.items.append(arg)
            self.usedslots += arg.weight

    def remove_items(self, arg):
        if isinstance(arg, list):
            for i in arg:
                if i in self.items:
                    self.items.remove(i)
        else:
            if arg in self.items:
                self.items.remove(arg)
