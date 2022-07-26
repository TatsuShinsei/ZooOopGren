from zoo.animals import Animal, Eagle, Lion, Tiger, Dolphin


class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class NoAnimalError(Exception):
    def __init__(self, message="This zoo got no animals, therefore it couldn't be initiated"):
        self.message = message
        super().__init__(self.message)


class Zoo(metaclass=NamedMeta):
    def __init__(self, animals: list[Animal or Tiger, Lion, Eagle, Dolphin] = None):
        if animals is None:
            raise NoAnimalError()

        self.animals = animals
        self.types = list()
        self.enclosures = int()
        self.dct = dict()

        self.necessary_enclosures()
        self.dict_by_types()

    def necessary_enclosures(self):
        for i in self.animals:
            if type(i) not in self.types:
                self.types.append(type(i))
        self.enclosures = len(self.types)

    def dict_by_types(self):
        self.dct = dict()
        for i in self.types:
            lst = list()
            for j in self.animals:
                if type(j) == i:
                    lst.append(j)
            self.dct[i] = lst

    def add_to_animals(self, arg: Animal | list[Animal]):
        if isinstance(arg, list):
            for i in arg:
                self.animals.append(i)
        else:
            self.animals.append(arg)

        self.necessary_enclosures()
        self.dict_by_types()

    def remove_from_animals(self, arg: Animal | list[Animal]):
        if isinstance(arg, list):
            for i in arg:
                if i in self.animals:
                    self.animals.remove(i)
                else:
                    print(f"couldn't remove {i}")
        else:
            if arg in self.animals:
                self.animals.remove(arg)
            else:
                print(f"couldn't remove {arg}")

        self.necessary_enclosures()
        self.dict_by_types()

    def order_by_tail(self) -> list:
        lst = list()
        for i in self.animals:
            if hasattr(i, "taillenght"):
                lst.append(i)
        lst.sort(key=lambda x: x.taillenght)
        lst = [f"{j.name} ({type(j)}) has a tail lenght of {j.taillenght} cm" for j in lst]
        lst.reverse()
        return lst

    def order_by_wingspan(self) -> list:
        lst = list()
        for i in self.animals:
            if hasattr(i, "wingspan"):
                lst.append(i)
        lst.sort(key=lambda x: x.wingspan)
        lst = [f"{j.name} ({type(j)}) has a wingspan of {j.wingspan} cm" for j in lst]
        lst.reverse()
        return lst

    def order_by_weight(self) -> list:
        lst = list()
        for i in self.animals:
            if hasattr(i, "weight"):
                lst.append(i)
        lst.sort(key=lambda x: x.weight)
        lst = [f"{j.name} ({type(j)}) has a weight of {j.weight} kg" for j in lst]
        lst.reverse()
        return lst

    def order_by_height(self) -> list:
        lst = list()
        for i in self.animals:
            if hasattr(i, "height"):
                lst.append(i)
        lst.sort(key=lambda x: x.height)
        lst = [f"{j.name} ({type(j)}) has a height of {j.height} cm" for j in lst]
        lst.reverse()
        return lst

    def order_by_maxjump(self) -> list:
        lst = list()
        for i in self.animals:
            if hasattr(i, "maxjump"):
                lst.append(i)
        lst.sort(key=lambda x: x.weight)
        lst = [f"{j.name} ({type(j)}) jumps a maximun of {j.maxjump} mc" for j in lst]
        lst.reverse()
        return lst

    def __str__(self):
        return f'''I'm a {type(self)}, and I have {len(self.animals)} animals
        with {len(self.types)} types, ({', '.join(map(str, self.types))})'''
