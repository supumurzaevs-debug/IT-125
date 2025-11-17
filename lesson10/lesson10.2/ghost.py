import random


class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.char = "G"


def move(self, maze):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = self.x + dx, self.y + dy
        if maze[ny][nx] != "#":
            self.x, self.y = nx, ny
            break