import re

with open('Day 4/input.txt', 'r') as file:
    text = file.read()
    
coind = re.findall(r"XMAS", text) + re.findall(r"SAMX", text)
lines = text.splitlines()
total = len(coind)

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i < len(lines)-3:
            if lines[i][j] == "X":
                if lines[i+1][j] == "M":
                    if lines[i+2][j] == "A":
                        if lines[i+3][j] == "S":
                            total += 1
        if i > 2:
            if lines[i][j] == "X":
                if lines[i-1][j] == "M":
                    if lines[i-2][j] == "A":
                        if lines[i-3][j] == "S":
                            total += 1
        if i < len(lines)-3 and j < len(lines[i])-3:
            if lines[i][j] == "X":
                if lines[i+1][j+1] == "M":
                    if lines[i+2][j+2] == "A":
                        if lines[i+3][j+3] == "S":
                            total += 1
        if i < len(lines)-3 and j > 2:
            if lines[i][j] == "X":
                if lines[i+1][j-1] == "M":
                    if lines[i+2][j-2] == "A":
                        if lines[i+3][j-3] == "S":
                            total += 1
        if i > 2 and j > 2:
            if lines[i][j] == "X":
                if lines[i-1][j-1] == "M":
                    if lines[i-2][j-2] == "A":
                        if lines[i-3][j-3] == "S":
                            total += 1
        if i > 2 and j < len(lines[i])-3:
            if lines[i][j] == "X":
                if lines[i-1][j+1] == "M":
                    if lines[i-2][j+2] == "A":
                        if lines[i-3][j+3] == "S":
                            total += 1
            
print(total)