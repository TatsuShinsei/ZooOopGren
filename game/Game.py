from os import system
from random import seed, randint, choice
from .objects.Player import Player
from .objects.Room import Room
from itertools import groupby

dire = [["north", "south"], ["south", "north"], ["east", "west"], ["west", "east"]]

seed(1234)

def clear():
    system("cls")


class NamedMeta(type):
    def __repr__(cls) -> str:
        return cls.__name__


class Game(metaclass=NamedMeta):
    def __init__(self, zoo):
        self.running = True
        self.zoo = zoo
        self.rooms = list()
        self.player = Player()
        self.__gen_rooms()
        self.__nrooms = self.zoo.enclosures

    def run(self):
        print(f"Welcome in your zoo {self.player.name}!")
        while self.running:
            clear()
            print("What do you wanna do?")
            print("1 - get zoo's infos")
            print("2 - move")
            print("3 - use item")
            print("4 - see rooms")
            print("5 - exit")
            match input():
                case "1":
                    clear()
                    self.__zoo_infos()
                case "2":
                    clear()
                    self.__move_player()
                case "3":
                    clear()
                    self.player.use_item()
                case "4":
                    clear()
                    for i in self.rooms:
                        print(i.name, i.animals, i.typeofanimals)
                        for wh, nb in i.neightboars.items():
                            print(f"   {wh} - {nb}")
                    input()
                case "5":
                    clear()
                    self.running = False
                case _:
                    clear()
                    print("sorry, can you repeat?")
                    input()

    def __zoo_infos(self):
        print("What do you wanna know of your zoo?")
        print("1 - ranking by weight")
        print("2 - ranking by height")
        print("3 - ranking by tail")
        print("4 - ranking by wingspan")
        print("5 - zoo population")
        print("any - cancel")
        match input():
            case "1":
                clear()
                pos = 1
                for i in self.zoo.order_by_weight():
                    print(f'{pos} - {i}')
                    pos += 1
                input("\npress any key to continue")
            case "2":
                clear()
                pos = 1
                for i in self.zoo.order_by_height():
                    print(f'{pos} - {i}')
                input("\npress any key to continue")
            case "3":
                clear()
                pos = 1
                for i in self.zoo.order_by_tail():
                    print(f'{pos} - {i}')
                input("\npress any key to continue")
            case "4":
                clear()
                pos = 1
                for i in self.zoo.order_by_wingspan():
                    print(f'{pos} - {i}')
                input("\npress any key to continue")
            case "5":
                clear()
                for key in self.zoo.dct.keys():
                    print(f"{key}:")
                    for animal in self.zoo.dct[key]:
                        print(f"   {animal}")
                input("\npress any key to continue")
            case _:
                clear()

    def __move_player(self):
        clear()
        print("where do you wanna go?")
        print("1 - up   | 3 - down")
        print("2 - left | 4 - right")
        print("any - cancel")
        match input():
            case "1":
                clear()
                self.player.move("up")
            case "2":
                clear()
                self.player.move("left")
            case "3":
                clear()
                self.player.move("down")
            case "4":
                clear()
                self.player.move("right")
            case _:
                clear()

    def __gen_rooms(self):
        nrooms = int(self.zoo.enclosures)

        def gen_room(r):
            poss = list()
            for j in range(randint(0, 3)):
                poss.append(choice(dire))

            poss.sort()
            poss = list(k for k, _ in groupby(poss))

            for pos in poss:
                if pos[1] not in r.neightboars.keys():
                    if len(self.rooms) <= self.zoo.enclosures:
                        nr = Room(type(chunk[0]), chunk, {pos[0]: r}, f'room {len(self.rooms)}')
                        self.rooms.append(nr)
                        gen_room(nr)

        parts = 4
        animals = self.zoo.dct

        chunked_animals = list()
        for key in animals.keys():
            sub_anml = animals[key]
            for i in range(0, len(sub_anml), parts):
                chunked_animals.append(sub_anml[i:i + parts])

        chunk = chunked_animals.pop()
        room = Room(type(chunk[0]), chunk, name="room 0")
        nrooms -= 1
        self.rooms.append(room)
        gen_room(room)

    def print_map(self):
        x = list([["██"] * int(4*1.5)])
        y = list(x*int(len(self.rooms)*1.5))

        hx = int(len(y[0])/2)
        print(hx)
        for x in y:
            x[hx]= "  "
        for ix in y:
            for i in ix:
                print(i, end="")
            print()
