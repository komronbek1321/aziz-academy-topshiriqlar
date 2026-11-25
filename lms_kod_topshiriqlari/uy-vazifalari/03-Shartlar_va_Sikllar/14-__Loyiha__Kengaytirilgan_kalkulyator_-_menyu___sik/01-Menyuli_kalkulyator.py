while True:
    op = int(input())
    if op == 0:
        break
    a = int(input())
    b = int(input())
            
    if op == 1:
        print(a + b)
    elif op == 2:
        print(a - b)
    elif op == 3:
        print(a * b)
    elif op == 4:
        if b == 0:
            print("Xato")
        else:
            print(a // b)
    else:
        print("Noma'lum")