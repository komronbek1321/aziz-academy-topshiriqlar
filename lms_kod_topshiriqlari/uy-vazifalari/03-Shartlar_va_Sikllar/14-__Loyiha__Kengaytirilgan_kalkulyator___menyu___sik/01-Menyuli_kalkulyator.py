while True:
    cmd = int(input())
    if cmd == 0:
        break
        
    a = int(input())
    b = int(input())
    
    if cmd == 1:
        print(a + b)
    elif cmd == 2:
        print(a - b)
    elif cmd == 3:
        print(a * b)
    elif cmd == 4:
        if b == 0:
            print("Xato")
        else:
            print(a // b)
    else:
         print("Noma'lum")