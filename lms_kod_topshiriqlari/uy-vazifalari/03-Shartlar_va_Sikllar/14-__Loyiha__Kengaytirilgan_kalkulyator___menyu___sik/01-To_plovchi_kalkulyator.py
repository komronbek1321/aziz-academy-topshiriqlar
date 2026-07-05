res = 0

while True:
    op = input().strip()
    if op == '=':
        break
                
    val = int(input())
    
    if op == '+':
        res += val
    elif op == '-':
        res -= val
    elif op == '*':
        res *= val
    elif op == '/':
        if val != 0:
            res //= val
print(res)                               