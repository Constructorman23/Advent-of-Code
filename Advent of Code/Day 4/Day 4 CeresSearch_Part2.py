import re

with open('Day 4/input.txt', 'r') as file:
    text = file.read()
    
lines = text.splitlines()
total = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i>0 and j>0 and i < len(lines)-1 and j < len(lines[i])-1:
            if lines[i][j] == "A":
                if lines[i+1][j+1] == "S":
                    if lines[i+1][j-1] == "M":
                        if lines[i-1][j-1] == "M":
                            if lines[i-1][j+1] == "S":
                                total += 1
        if i>0 and j>0 and i < len(lines)-1 and j < len(lines[i])-1:
            if lines[i][j] == "A":
                if lines[i+1][j+1] == "S":
                    if lines[i+1][j-1] == "S":
                        if lines[i-1][j-1] == "M":
                            if lines[i-1][j+1] == "M":
                                total += 1
        if i>0 and j>0 and i < len(lines)-1 and j < len(lines[i])-1:
            if lines[i][j] == "A":
                if lines[i+1][j+1] == "M":
                    if lines[i+1][j-1] == "S":
                        if lines[i-1][j-1] == "S":
                            if lines[i-1][j+1] == "M":
                                total += 1
        if i>0 and j>0 and i < len(lines)-1 and j < len(lines[i])-1:
            if lines[i][j] == "A":
                if lines[i+1][j+1] == "M":
                    if lines[i+1][j-1] == "M":
                        if lines[i-1][j-1] == "S":
                            if lines[i-1][j+1] == "S":
                                total += 1
                
            
print(total)