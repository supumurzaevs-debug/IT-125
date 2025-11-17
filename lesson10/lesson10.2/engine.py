from map_data import maze
from player import Player

def render(maze, player):
    for y in range(len(maze)):
        line = list(maze[y])
        if y == player.y:
            line[player.x] = player.char
        print("".join(line))


def start_game(name):
    player = Player(name, 1, 1)

    while True:
        render(maze, player)

        move = input("Ваш ход (w/a/s/d): ")

        new_x, new_y = player.x, player.y

        if move == "w":
            new_y -= 1
        elif move == "s":
            new_y += 1
        elif move == "a":
            new_x -= 1
        elif move == "d":
            new_x += 1
        else:
            print("Используйте только w/a/s/d!")
            continue

        cell = maze[new_y][new_x]

        if cell == "#":
            print("Стена! Нельзя туда.")
            continue

        if cell == "*":
            print("Вы выбрались! Победа!")
            break

        player.x, player.y = new_x, new_y
