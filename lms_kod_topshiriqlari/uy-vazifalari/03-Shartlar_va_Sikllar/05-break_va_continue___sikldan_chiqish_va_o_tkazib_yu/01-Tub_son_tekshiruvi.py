n = int(input())

if n < 2:
    print("yo'q")
else:
    tub = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            tub = False
            break
        i += 1
        
    if tub:
        print("ha")
    else:
        print("yo'q")