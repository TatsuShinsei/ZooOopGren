from game.objects.Room import Room
from random import choice, randint, seed

seed(1234)

a = "wasd"
b = ["wasd"]


rooms = []

kk = []

lastpos = ""
lastr = Room(a, b)
print(lastr)


for i in rooms:
    print(i.neightboars)
