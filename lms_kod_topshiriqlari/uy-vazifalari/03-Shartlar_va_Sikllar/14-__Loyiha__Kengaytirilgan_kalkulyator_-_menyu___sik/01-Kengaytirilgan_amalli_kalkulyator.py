eng_katta = None
while True:
    amal = int(input())
    if amal == 0:
        break
    a = int(input())
    b = int(input())
    natija = None
    yaroqli = True
            
    if amal == 1:
        natija = a + b
    elif amal == 2:
        natija = a - b
    elif amal == 3:
        natija = a * b
    elif amal == 4:
        if b == 0:
            yaroqli = False
        else:
            natija = a // b
    elif amal == 5:
            natija = a ** b
    elif amal == 6:
        if b == 0:
            yaroqli = False
        else:
            natija = a % b    
    else:
        yaroqli = False
        
    if yaroqli and natija is not None:
        print(natija)
        if eng_katta is None or natija > eng_katta:
            eng_katta = natija
if eng_katta is not None:   
    print(f"Eng katta natija: {eng_katta}")