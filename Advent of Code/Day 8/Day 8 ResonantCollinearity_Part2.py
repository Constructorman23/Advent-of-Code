import re

with open('Day 8/input.txt', 'r') as file:
    text = file.read()

text_filtered = list(dict.fromkeys(re.sub(r'[^a-zA-Z0-9]', '', text)))

total = 0

lines = [list(linea) for linea in text.splitlines()]

antinodes = set()

for chara in text_filtered:
    posiciones = []
    
    for i, linea in enumerate(lines):
        for j, char in enumerate(linea):
            if char == chara:
                posiciones.append((i, j))
    
    for i in range(len(posiciones) - 1):
        for j in range(i + 1, len(posiciones)):
            pos1 = posiciones[i]
            pos2 = posiciones[j]
            
            dx = pos2[1] - pos1[1]
            dy = pos2[0] - pos1[0]
            
            antinode1 = (pos1[0] - dy, pos1[1] - dx)
            antinode2 = (pos2[0] + dy, pos2[1] + dx)
            
            if 0 <= antinode1[0] < len(lines) and 0 <= antinode1[1] < len(lines[0]):
                antinodes.add(antinode1)
            if 0 <= antinode2[0] < len(lines) and 0 <= antinode2[1] < len(lines[0]):
                antinodes.add(antinode2)

total = len(antinodes)

print(total)
