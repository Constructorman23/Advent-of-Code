import re

with open('Day 3/input.txt', 'r') as file:
    text = file.read()

total = 0
pos = 0
dont = r"don't\(\)"
do = r"do\(\)"
mul = r"mul\((\d+),(\d+)\)"

pause = False
indices = []
coind = []

while pos < len(text):
    match_dont = re.search(dont, text[pos:])
    match_do = re.search(do, text[pos:])
    match_mul = re.search(mul, text[pos:])


    pos_dont = match_dont.start() + pos if match_dont else float('inf')
    pos_do = match_do.start() + pos if match_do else float('inf')
    pos_mult = match_mul.start() + pos if match_mul else float('inf')

    if pos_dont < pos_do and pos_dont < pos_mult:
        pause = True
        pos = pos_dont + len("dont()")
    elif pos_do < pos_dont and pos_do < pos_mult:
        pause = False
        pos = pos_do + len("do()")
    elif pos_mult < pos_dont and pos_mult < pos_do:
        if not pause:
            indices.append(pos_mult)
            coind.append((match_mul.group(1), match_mul.group(2)))
        pos = pos_mult + len(match_mul.group())
    else:
        break

for a, b in coind:
    mult = int(a) * int(b)
    total += mult

print(total)
