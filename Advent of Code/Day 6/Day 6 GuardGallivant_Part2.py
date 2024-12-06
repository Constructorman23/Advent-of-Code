with open('Day 6/input.txt', 'r') as file:
    text = file.read()

lines = text.splitlines()
lines = list(map(list, lines))

posini = (0, 0, 0)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            posini = (i, j, 0)
        if lines[i][j] == ">":
            posini = (i, j, 1) 
        if lines[i][j] == "v":
            posini = (i, j, 2)
        if lines[i][j] == "<":
            posini = (i, j, 3)

looped = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#" or (i == posini[0] and j == posini[1]):
            continue
        else:
            lines[i][j] = "#"
            visited = []
            loop = False
            pos = list(posini)
            turn = False
            while not loop:
                try:
                    if (pos[0], pos[1], pos[2]) in visited:
                        loop = True
                        break
                    else:
                        if not turn:
                            visited.append((pos[0], pos[1], pos[2]))
                            
                        turn = False

                        if pos[2] == 0:
                            if lines[pos[0] - 1][pos[1]] == "#":
                                pos[2] = (pos[2] + 1) % 4
                                turn = True
                            else:
                                pos[0] -= 1
                        elif pos[2] == 1:
                            if lines[pos[0]][pos[1] + 1] == "#":
                                pos[2] = (pos[2] + 1) % 4
                                turn = True
                            else:
                                pos[1] += 1
                        elif pos[2] == 2:
                            if lines[pos[0] + 1][pos[1]] == "#":
                                pos[2] = (pos[2] + 1) % 4
                                turn = True
                            else:
                                pos[0] += 1
                        elif pos[2] == 3:
                            if lines[pos[0]][pos[1] - 1] == "#":
                                pos[2] = (pos[2] + 1) % 4
                                turn = True
                            else:
                                pos[1] -= 1
                    
                    if pos[0] < 0 or pos[0] >= len(lines) or pos[1] < 0 or pos[1] >= len(lines[0]):
                        break

                except IndexError:
                    break

            if loop:
                looped += 1
                print(i, j)
                print(visited)

            lines[i][j] = "."

print(looped)
