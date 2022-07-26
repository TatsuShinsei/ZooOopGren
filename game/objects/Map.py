from numpy import floor
from . import Room


class Map:
    def __init__(self, rooms: list[Room]):
        self.rooms = rooms
        self.map = list()
        self.roomsdone = list()

    def create_map(self):
        tile = "  "
        self.roomsdone = list()

        def edit_map(r: Room, rix, riy):
            self.roomsdone.append(r)
            for key, value in r.neightboars.items():
                if value not in self.roomsdone:
                    match key:
                        case "north":
                            nix, niy = rix, riy + 1
                            self.map[niy][nix] = f'{value.name[0]}{value.name[-1]}'
                            edit_map(value, nix, niy)
                        case "south":
                            nix, niy = rix, riy - 1
                            self.map[niy][nix] = f'{value.name[0]}{value.name[-1]}'
                            edit_map(value, nix, niy)
                        case "west":
                            nix, niy = rix + 1, riy
                            self.map[niy][nix] = f'{value.name[0]}{value.name[-1]}'
                            edit_map(value, nix, niy)
                        case "east":
                            nix, niy = rix + 1, riy
                            self.map[niy][nix] = f'{value.name[0]}{value.name[-1]}'
                            edit_map(value, nix, niy)

        self.map = [[tile for _ in range(int(len(self.rooms)*2))] for _ in range(int(len(self.rooms)*2))]
        hx = int(floor(len(self.map[0]) / 2)) - 1
        hy = int(floor(len(self.map) / 2)) - 1

        self.map[hy][hx] = "R0"

        edit_map(self.rooms[0], hx, hy)

        kk = list()
        for lx in self.map:
            if len(set(lx)) > 1:
                kk.append(lx)
        smolindex = int(len(self.rooms)*2)
        bigindex = 0
        for k in kk:
            for ww in k:
                if ww != tile:
                    ind = k.index(ww)
                    if ind < smolindex:
                        smolindex = ind
                    if ind > bigindex:
                        bigindex = ind

        for wasd in kk:
            for i in range(bigindex - smolindex):
                if not smolindex+i > bigindex:
                    print(wasd[smolindex+i], end="")
            print()
