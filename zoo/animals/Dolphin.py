from .animal import Animal


class Dolphin(Animal):
    def __init__(self, maxjump: int, name, gender, favfood, age, dateofjoin, weight, height):
        super().__init__(name, gender, favfood, age, dateofjoin, weight, height)
        self.maxjump = maxjump

    def __repr__(self):
        return "Dolphin"
