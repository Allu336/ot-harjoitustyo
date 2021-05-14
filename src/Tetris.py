import pygame

class Tetris():
    def __init__(self):
        self.grid = []

    def create_grid(self):
        for row in range(0,23):
            self.grid.append([".",".",".",".",".",".",".",".",".","."])
        grid = self.grid

    def update_grid(self, old_cordinates, new_cordinates):
        for k in old_cordinates:
            if self.grid[k[0][0]][k[0][1]] == "2":
                continue
            self.grid[k[0][0]][k[0][1]] = "."
        for k in new_cordinates:
            if k[1] == "1":
                self.grid[k[0][0]][k[0][1]] = "1"
    

    