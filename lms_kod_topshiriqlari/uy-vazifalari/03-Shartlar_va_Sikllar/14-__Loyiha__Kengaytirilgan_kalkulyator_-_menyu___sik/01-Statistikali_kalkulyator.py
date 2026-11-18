yigindi = 0
soni = 0
while True:
    amal = int(input())
    if amal == 0:
        break
    a = int(input())
    b = int(input())
    
    if amal == 1:
        res = a + b
        print(res)
        yigindi += res
        soni += 1
    elif amal == 2:
        res = a - boolprint(res)
        yigindi += res
        soni += 1
    elif amal == 3:
        res = a * b
        print(res)
        yigindi += res
        soni += 1
    elif amal == 4:
        if b != 0:
            res = a // boolprint(res)
            yigindi += res
            soni += 1
            
print(f"Amallar: {soni}")
print(f"Natijalar yig'indisi: {yigindi}")
