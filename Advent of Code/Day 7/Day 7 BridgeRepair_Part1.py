
with open('Day 7/input.txt', 'r') as file:
    lines = file.read().splitlines()

obj = []
opr = []
total = 0 
   
for line in lines:
    r, o = line.split(":")
    
    obj.append(int(r.strip()))
    opr.append(list(map(int, o.split())))


for i in range(len(obj)):
    calibrated = False
    n = 2**(len(opr[i])-1)
    bits = (len(opr[i])-1)
    print(opr[i])
    for j in range(n):
        operators = []
        num = j
        for _ in range(bits):
            bit = num%2
            operators.insert(0,"*" if bit == 0 else "+")
            num //= 2
        res = opr[i][0]
        for k,operator in enumerate(operators):
            digit = opr[i][k+1]
            
            if operator == "*":
                res *= digit
            elif operator == "+":
                res += digit
            
        if res == obj[i]:
            calibrated = True
            break
        
    if calibrated:
        total+=obj[i]
        
print(total)