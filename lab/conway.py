import curses
import numpy as np
import time

from collections import defaultdict
from enum import Enum
from typing import List


class State(Enum):
    ''' enum class to represent possible cell states '''
    dead = 0
    alive = 1


class Board:
    ''' Board class to represent the game board '''
    def __init__(self, m : int, n : int, init : List[List[int]]):
        self.m = m   # the number of rows
        self.n = n   # the number of columns
        self.board_ = [
            [State(init[i][j]) for j in range(self.n)] for i in range(self.m)
        ]

    def __str__(self) -> str:
        ''' return the __str__ representation of a Board object
            * represents a live cell, and a space represents a dead one
        '''
        return '\n'.join([
            ''.join(
                    ['*' if cell.value else ' ' for cell in row]
            ) for row in self.board_]
        )

    @property
    def population(self):
        ''' population — the number of live cells on the board '''
        return sum(cell.value for row in self.board_ for cell in row)

    def count_live_neighbours(self, x : int, y : int) -> int:
        ''' count the live neighbours of a cell '''
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i == x and j == y) or i < 0 or j < 0:
                    continue
                # handle IndexErrors raised during invalid indexing operations 
                try:
                    count += self.board_[i][j].value
                except IndexError:
                    continue

        return count

    def next_cell_state(self, x : int, y : int) -> State:
        count = self.count_live_neighbours(x, y)
        cur_state = self.board_[x][y]
        # determine the next state based on the current state and 
        # number of live neighbours 
        if count in {2, 3} and cur_state == State.alive:
            return cur_state
        elif count == 3 and cur_state == State.dead:
            return State.alive

        return State.dead

    def next_board_state(self) -> List[List[State]]: 
        ''' return board configuration for the next state '''    
        return [
            [self.next_cell_state(i, j) for j in range(self.n)] for i in range(self.m)
        ]

    def advance_state(self):
        ''' update the board configuration with the config for the next state '''
        self.board_ = self.next_board_state()

    def has_live_cells(self) -> bool:
        ''' return whether there are any live cells or not '''
        return any(cell.value for row in self.board_ for cell in row)


if __name__ == '__main__':
    arr = np.random.choice([0, 1], (20, 100), p=[0.90, 0.1]) 
    board = Board(arr.shape[0], arr.shape[1], init=arr.tolist())

    step = 0
    while board.has_live_cells():
        step += 1
        print(board)
        print(f'{step} {board.population}')
        board.advance_state()

        time.sleep(.1)