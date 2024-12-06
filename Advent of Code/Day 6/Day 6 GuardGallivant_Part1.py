import re

with open('Day 6/input.txt', 'r') as file:
    text = file.read()

lines = text.splitlines()

lines = list(map(list, lines))

pos = (0,0)
facing = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "^":
            pos = [i,j]
            facing = 0
        if lines[i][j] == ">":
            pos = [i,j]
            facing = 1
        if lines[i][j] == "v":
            pos = [i,j]
            facing = 2
        if lines[i][j] == "<":
            pos = [i,j]
            facing = 3
      
out = False
while not out:
    try:
        lines[pos[0]][pos[1]] = "X"
        if facing == 0:
            if lines[pos[0]-1][pos[1]] == "#":
                facing += 1
            else:
                pos[0] -= 1
        elif facing == 1:
            if lines[pos[0]][pos[1]+1] == "#":
                facing += 1
            else:
                pos[1] += 1
        elif facing == 2:
            if lines[pos[0]+1][pos[1]] == "#":
                facing += 1
            else:
                pos[0] += 1
        elif facing == 3:
            if lines[pos[0]][pos[1]-1] == "#":
                facing = 0
            else:
                pos[1] -= 1                
    except IndexError:
        break

text = list(map("".join,lines))
text = "\n".join(text)
coind = re.findall("X",text)
res = len(coind)


print(res)
        
                
            
           
             