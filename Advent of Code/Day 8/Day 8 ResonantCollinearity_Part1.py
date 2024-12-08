import re
import math
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
            gcd = abs(math.gcd(dx, dy))
            dx //= gcd
            dy //= gcd

            x, y = pos1[0], pos1[1]
            while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
                antinodes.add((x, y))
                x -= dy
                y -= dx

            x, y = pos2[0], pos2[1]
            while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
                antinodes.add((x, y))
                x += dy
                y += dx

total = len(antinodes)

print(total)
