import numpy as np


class Game:
    __name__ = "Game"

    def __init__(self, array):
        self._dim = np.shape(array)
        self._array = np.asarray(array).copy()
        self._hole = list(np.where(self._array == 0))  # (y, x)

    def __str__(self):
        board = ""
        for i in self._array:
            for j in i:
                board = "".join((board, f"{j}\t"))
            board = board + "\n"
        return board

    def move_to_left(self):
        if self._hole[1] > 0:
            self._array[self._hole[0], self._hole[1]] = self._array[self._hole[0], self._hole[1] - 1]
            self._array[self._hole[0], self._hole[1] - 1] = 0
            self._hole[1] = self._hole[1] - 1

    def move_to_right(self):
        if self._hole[1] < self._dim[1] - 1:
            self._array[self._hole[0], self._hole[1]] = self._array[self._hole[0], self._hole[1] + 1]
            self._array[self._hole[0], self._hole[1] + 1] = 0
            self._hole[1] = self._hole[1] + 1

    def move_to_up(self):
        if self._hole[0] > 0:
            self._array[self._hole[0], self._hole[1]] = self._array[self._hole[0] - 1, self._hole[1]]
            self._array[self._hole[0] - 1, self._hole[1]] = 0
            self._hole[0] = self._hole[0] - 1

    def move_to_down(self):
        if self._hole[0] < self._dim[0] - 1:
            self._array[self._hole[0], self._hole[1]] = self._array[self._hole[0] + 1, self._hole[1]]
            self._array[self._hole[0] + 1, self._hole[1]] = 0
            self._hole[0] = self._hole[0] + 1

    def get_board(self):
        return self._array

    def is_done(self, solution):
        solution = np.array(solution)
        result = self._array - solution
        if np.abs(result).sum() == 0:
            return True
        return False
