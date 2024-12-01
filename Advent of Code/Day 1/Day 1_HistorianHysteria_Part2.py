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
        
for i in range(len(right)):
    cont = 0
    for j in range(len(left)):
        if right[i] == left[j]:
            cont += 1
    sum += cont * right[i]
    
print(sum)