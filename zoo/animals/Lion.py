from .animal import Animal


class Lion(Animal):
    def __init__(self, taillenght: int, name, gender, favfood, age, dateofjoin, weight, height):
        super().__init__(name, gender, favfood, age, dateofjoin, weight, height)
        self.taillenght = taillenght

    def __repr__(self):
        return "Lion"
