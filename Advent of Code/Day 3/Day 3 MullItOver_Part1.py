import re

with open('Day 3/input.txt', 'r') as file:
    text = file.read()

total = 0
coind = re.findall(r"mul\((\d+),(\d+)\)", text)

for a, b in coind:
    mult = int(a) * int(b)
    total += mult
    
print(total)