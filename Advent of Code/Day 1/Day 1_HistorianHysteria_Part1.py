with open('input.txt', 'r') as archivo:
    aux=archivo.read().split()
    
sum = 0
right=[]
left=[]
for i in range(len(aux)):
    if i % 2 == 0:
        right.append(int(aux[i]))
    else:
        left.append(int(aux[i]))

right.sort()
left.sort()

for i in range(len(right)):
    if right[i] > left[i]:
        sum += right[i]-left[i]
    else:
        sum += left[i]-right[i]
        
print(sum)