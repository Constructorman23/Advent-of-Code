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
incorrect_pages=[]
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
    else:
        incorrect_pages.append(page)

print(res)

res2 = 0
for page in incorrect_pages:
    coind = [
        rule for rule in rules
        if all(num in page for num in rule)
    ]
    
    i = 0
    while i < len(page) - 1:
        swapped = False 
        for c in coind:
            if page[i] == c[1] and i + 1 < len(page):
                if c[0] == page[i+1]:
                    aux = page[i+1]
                    page[i+1] = page[i]
                    page[i] = aux
                    swapped= True
        if swapped:
            i = 0
        else:
            i += 1
        
    res2 += page[len(page)//2]
                    
    
print(res2)