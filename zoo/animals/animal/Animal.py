class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class Animal(metaclass=NamedMeta):
    def __init__(self, name: str, gender: str, favfood: str, age: int, dateofjoin: str, weight: int | float,
                 height: int):
        self.name = name
        self.gender = gender
        self.favFood = favfood
        self.age = age
        self.dateofjoin = dateofjoin
        self.weight = weight
        self.height = height

    def __str__(self):
        return f"I'm {self.name} and i'm a {type(self)}"
