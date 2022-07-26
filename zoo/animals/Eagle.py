from .animal import Animal


class Eagle(Animal):
    def __init__(self, wingspan: int, name, gender, favfood, age, dateofjoin, weight, height):
        super().__init__(name, gender, favfood, age, dateofjoin, weight, height)
        self.wingspan = wingspan

    def __repr__(self):
        return "Eagle"
