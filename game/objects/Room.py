from zoo.animals import Animal, Dolphin, Tiger, Lion, Eagle


class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class Room(metaclass=NamedMeta):
    def __init__(self, typeofanimals: Animal | Dolphin | Lion |Tiger | Eagle, animals:list[Animal | Dolphin and Tiger and Eagle and Lion], neightboars=None, name="Room"):
        if neightboars is None:
            neightboars = dict()
        self.typeofanimals = typeofanimals
        self.animals = [a.name for a in animals]
        self.neightboars = neightboars
        self.name = name

        if self.neightboars:
            self.__adm_neightboars()

    def __adm_neightboars(self):
        for k, v in dict(self.neightboars).items():
            match k:
                case "north":
                    v.neightboars["south"] = self
                case "south":
                    v.neightboars["north"] = self
                case "east":
                    v.neightboars["west"] = self
                case "west":
                    v.neightboars["east"] = self
                case _:
                    print(f"{k} is not a valid direction, {v}'s neightboars not edited")

    def __str__(self):
        return self.name
