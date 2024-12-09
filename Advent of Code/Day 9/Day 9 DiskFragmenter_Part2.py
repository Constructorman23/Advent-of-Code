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


file_ids = sorted(set(disk) - {"."}, reverse=True)
for file_id in file_ids:
    file_blocks = []
    for i,block in enumerate(disk):
        if block == file_id:
            file_blocks.append(i)
    if not file_blocks:
        continue
    
    len_file = len(file_blocks)
    rightmost_block = max(file_blocks)
    
    spacepos=-1
    spacelen=0
    for i in range(rightmost_block):
        if disk[i] == ".":
            if spacepos == -1:
                spacepos = i
            spacelen+=1
        else:
            spacepos = -1
            spacelen = 0
            
        if spacelen == len_file:
            for j in range(len_file):
                disk[spacepos+j] = file_id
                
            for index in file_blocks:
                disk[index] = "."
            break
total=0
for i in range(len(disk)):
    if disk[i] != ".":
        total+=i*disk[i]
print(total)