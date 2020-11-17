class State():
    def __init__(self, player_x, player_y, box_x, box_y):
        self._player_loc = (player_x, player_y)
        self._box_loc = (box_x, box_y)
    
    def __eq__(self, o):
        return isinstance(o, State) and self._player_loc == o._player_loc and self._box_loc == o._box_loc

    def __hash__(self):
        return hash((self._player_loc, self._box_loc))


class Labyrinth():
    def __init__(self, r):
        self._r = r
        self._m = len(r)
        self._n = len(r[0])
        for y in range(self._m):
            xx = r[y].find("X")
            if xx != -1:
                self._xloc = (xx, y)
            yx = r[y].find("Y")
            if yx != -1:
                self._yloc = (yx, y)
            bx = r[y].find("B")
            if bx != -1:
                self._bloc = (bx, y)




def count(r):
    lab = Labyrinth(r)
    pass

if __name__ == "__main__":
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
    print(count(r)) # 18
