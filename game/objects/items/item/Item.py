class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class Item(metaclass=NamedMeta):
    def __init__(self, name: str, description: str, weight: int):
        self.name = name
        self.description = description
        self.weight = weight

    def use(self):
        pass
