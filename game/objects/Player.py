from . import Bag, Item


class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class MaxSoltsExeption(Exception):
    def __init__(self, message="Maxximun ammount of items raeached, douldn't add the item to the inventory"):
        self.message = message
        super().__init__(self.message)


class Player(metaclass=NamedMeta):
    def __init__(self, hp=20):
        self.bag = Bag(list())
        self.name = input("What's your name?\n")
        self.hp = hp
        self.maxslots = 2
        self.usedslots = int()
        self.items = list()
        self.pos = [0, 0]

    def add_items(self, arg: Item or list[Item]):
        if isinstance(arg, list):
            for i in arg:
                if self.usedslots + i.weight < self.maxslots:
                    self.items.append(i)
                    self.usedslots += i.weight
                else:
                    self.bag.add_items(i)
        else:
            if self.usedslots + arg.weight < self.maxslots:
                self.items.append(arg)
                self.usedslots += arg.weight
            else:
                self.bag.add_items(arg)

    def remove_items(self, arg: Item or list[Item]):
        if isinstance(arg, list):
            for i in arg:
                if i in self.items:
                    self.items.remove(i)
                else:
                    if i in self.bag.items:
                        self.bag.remove_items(i)
        else:
            if arg in self.items:
                self.items.remove(arg)
            else:
                if arg in self.bag.items:
                    self.bag.remove_items(arg)

    def move(self, arg:str):
        match arg:
            case "up":
                self.pos[1] += 1
            case "down":
                self.pos[1] -= 1
            case "left":
                self.pos[0] -= 1
            case "right":
                self.pos[0] += 1
        print(f"new position: x = {self.pos[0]} | y = {self.pos[1]}")
        input("press any key to continue")

    def use_item(self):
        if self.items or self.bag.items:
            print("where do you wanna pick the item from?")
            print("1 - player's inventory | 2 - bag's inventory")
            c = 1
            match input():
                case "1":
                    if self.items:
                        c = 1
                        print("player inventory:")
                        for i in self.items:
                            print(f"   {c} - {i.name}")
                        try:
                            itemn = int(input()) - 1
                            self.items[itemn].use()
                        except IndexError:
                            print("no item in such slot")
                        except ValueError:
                            print("incorrect input")
                case "2":
                    if self.bag and self.bag.items:
                        print("bag inventory:")
                        for i in self.bag.items:
                            print(f"   {c} - {i.name}")
                        try:
                            itemn = int(input()) - 1
                            self.bag.items[itemn].use()
                        except IndexError:
                            print("no item in such slot")
                        except ValueError:
                            print("incorrect input")
            input()
            return
        print("no items aviable, sorry")
        input()
