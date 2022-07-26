import names
from game import Game
from game.objects.items import Key, MagnifyingGlass
from zoo import Zoo
from zoo.animals import Lion, Tiger, Eagle

foods = ["food1", "food2", "food3", "food4", "food5", "food6", "food7", "food8", "food9", "food10"]

seed = 1234
random = names.random
random.seed(seed)

total_animals = list()


def gen_lion():
    gender = random.choice(['male', 'female'])
    name = names.get_first_name(gender=gender)
    favfood = random.choice(foods)
    age = random.randint(5, 12)
    dateofjoin = f"{random.randint(0, 30)}/{random.randint(1, 12)}/{2022 - age + random.randint(0, age)}"
    weight = random.randint(120, 220)
    height = random.randint(80, 140)
    taillenght = random.randint(60, 120)
    lion = Lion(name=name, gender=gender, favfood=favfood, age=age, dateofjoin=dateofjoin, weight=weight,
                height=height, taillenght=taillenght)
    return lion


def gen_tiger():
    gender = random.choice(['male', 'female'])
    name = names.get_first_name(gender=gender)
    favfood = random.choice(foods)
    age = random.randint(5, 12)
    dateofjoin = f"{random.randint(0, 30)}/{random.randint(1, 12)}/{2022 - age + random.randint(0, age)}"
    weight = random.randint(120, 220)
    height = random.randint(80, 140)
    taillenght = random.randint(60, 120)
    tiger = Tiger(name=name, gender=gender, favfood=favfood, age=age, dateofjoin=dateofjoin, weight=weight,
                  height=height, taillenght=taillenght)
    return tiger


def gen_eagle():
    gender = random.choice(['male', 'female'])
    name = names.get_first_name(gender=gender)
    favfood = random.choice(foods)
    age = random.randint(5, 32)
    dateofjoin = f"{random.randint(1, 30)}/{random.randint(1, 12)}/{2022 - age + random.randint(0, age)}"
    weight = round(random.uniform(0.500, 7.2), 3)
    height = random.randint(80, 260)
    wingspan = random.randint(50, 300)
    eagle = Eagle(name=name, gender=gender, favfood=favfood, age=age, dateofjoin=dateofjoin, weight=weight,
                  height=height, wingspan=wingspan)
    return eagle


for i in range(12):
    total_animals.append(gen_lion())

for i in range(3):
    total_animals.append(gen_tiger())

for i in range(4):
    total_animals.append(gen_eagle())

tatsu_zoo = Zoo(total_animals)

game = Game(tatsu_zoo)

key = Key("Key 1", "normal emplyee key", 1, 1)
maggalss = MagnifyingGlass("Mag MK1", "Just a magnifying glass", 2)

game.player.add_items([key, maggalss])

print(game.rooms)

game.print_map()

