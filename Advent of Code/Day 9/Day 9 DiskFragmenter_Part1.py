with open('Day 9/input.txt', 'r') as file:
    text = file.read()
    
text = list(map(int, text))

j = 0
disk =[]
for i in range(len(text)):
    if i%2==0:
        for k in range(text[i]):
            disk.append(j)    
        j+=1
    else:
        for k in range(text[i]):
            disk.append(".")

loop = True
i = 0
while loop:
    if disk[i] == ".":
        last = disk.pop()
        while last == ".":
            last = disk.pop()
        disk[i] = last
    if i < len(disk)-1:
        i+=1
    else:
        break
total=0
for i in range(len(disk)):
    total+=i*disk[i]
    
print(total)