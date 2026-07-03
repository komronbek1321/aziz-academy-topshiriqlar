n = int(input())

if n < 2:
    print("TUB EMAS")
else:
    tub = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            tub = False
            break
            
    if tub:
        print("TUB")
    else:
        print("TUB EMAS")