with open('Day 2/input.txt', 'r') as file:
    lines = file.read().splitlines()

total = 0
lines2 = []

def is_safe(line):
    for i in range(len(line)-1):
        if abs(line[i]-line[i+1])<1 or abs(line[i]-line[i+1])>3:
            return False
        if (line[i] < line[i + 1] and line[0] > line[1]) or (line[i] > line[i + 1] and line[0] < line[1]):
            return False
    return True


for line in lines:
    report = list(map(int, line.split()))

    if is_safe(report):
        total += 1
        continue
    
    
    dumper = False
    for i in range(len(line)):
        report2 = report[:i] + report[i + 1:]
        if is_safe(report2):
            dumper=True
            break
        
    if dumper:
        total +=1

print(total)
    