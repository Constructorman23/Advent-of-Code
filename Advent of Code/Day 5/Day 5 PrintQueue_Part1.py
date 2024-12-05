import re

rules = []
pages = []

with open('Day 5/input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if re.match(r"^\d+\|\d+$", line):
            rules.append(line)
        elif re.match(r"^\d+(,\d+)*$",line):
            pages.append(line)
            
for i in range(len(rules)):
    rules[i] = list(map(int, rules[i].split('|')))
        
for i in range(len(pages)):
    pages[i] = list(map(int, pages[i].split(',')))

res = 0
for page in pages:
    coind = [
        rule for rule in rules
        if all(num in page for num in rule)
    ]
    
    correct = True
    for i in range(len(page)-1):
        for c in coind:
            if page[i] == c[1]:
                if c[0] == page[i+1]:
                    correct = False
                    
    if correct:
        res += page[len(page)//2]

print(res)