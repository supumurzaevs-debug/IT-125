box = [
    "###########################",
    "# #               #       #",
    "# ####  ######    ###  #  #",
    "#       #              # *#",
    "###########################"
]

player_x = 1  
player_y = 1  

while True:
    
    for y in range(len(box)):
        line = box[y]
        if y == player_y:
            line = line[:player_x] + "A" + line[player_x + 1:]
        print(line)
    
    
    move = input("Ваш ход (w/a/s/d): ")
    new_x, new_y = player_x, player_y
    
    if move == "w":
        new_y -= 1
    elif move == "s":
        new_y += 1
    elif move == "a":
        new_x -= 1
    elif move == "d":
        new_x += 1
    else:

        print("Используй только w/a/s/d")
        continue
    
    
    if box[new_y][new_x] == "#":
        print("Ты врезался в стену, игра закончена.")
        break
    elif box[new_y][new_x] == "*":
        print("Ты выбрался") 
        break
    else:
        player_x, player_y = new_x, new_y
