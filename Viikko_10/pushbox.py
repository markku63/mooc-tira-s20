from collections import deque


class Labyrinth:
    def __init__(self, r):
        self._r = r
        self._m = len(r)
        self._n = len(r[0])
        player_x = -1
        player_y = -1
        box_x = -1
        box_y = -1
        for y in range(self._m):
            xx = r[y].find("X")
            if xx != -1:
                player_x = xx
                player_y = y
            yx = r[y].find("Y")
            if yx != -1:
                self._yloc = (yx, y)
            bx = r[y].find("B")
            if bx != -1:
                box_x = bx
                box_y = y
        self._init_state = (player_x, player_y, box_x, box_y)

    def _solved(self, state):
        # onko laatikko maalissa?
        return (state[2], state[3]) == self._yloc

    def _push(self, state, move):
        # ollaanko laatikon vieressä ja voiko sitä työntää?
        if (
            self._r[state[1] + move[1]][state[0] + move[0]] != "#"
            and state[0] + move[0] == state[2]
            and state[1] + move[1] == state[3]
            and self._r[state[1] + 2 * move[1]][state[0] + 2 * move[0]] != "#"
        ):
            return (
                state[0] + move[0],
                state[1] + move[1],
                state[2] + move[0],
                state[3] + move[1],
            )
        else:
            return None

    def _move(self, state, move):
        # voiko haluttuun suuntaan siirtyä?
        if self._r[state[1] + move[1]][state[0] + move[0]] == "#" or (
            state[0] + move[0] == state[2] and state[1] + move[1] == state[3]
        ):
            return None
        else:
            return (state[0] + move[0], state[1] + move[1], state[2], state[3])

    def solve(self):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = {}
        dist[self._init_state] = 0
        queue = deque([self._init_state])
        while len(queue) > 0:
            curr_state = queue.popleft()
            if self._solved(curr_state):
                return dist[curr_state]
            for move in moves:
                tmp = self._push(curr_state, move)
                if not tmp:
                    # työntö ei mahdollinen
                    tmp = self._move(curr_state, move)
                if tmp and tmp not in dist:
                    dist[tmp] = dist[curr_state] + 1
                    queue.append(tmp)
        return -1


def count(r):
    lab = Labyrinth(r)
    return lab.solve()


if __name__ == "__main__":
    r = [
        "########",
        "#......#",
        "#.#.Y#.#",
        "#.#B.#.#",
        "#..X.#.#",
        "#.#..#.#",
        "########",
    ]
    print(count(r))  # 18
