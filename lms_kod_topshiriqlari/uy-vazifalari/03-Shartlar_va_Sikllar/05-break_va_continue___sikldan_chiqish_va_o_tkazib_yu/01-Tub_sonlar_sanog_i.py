tub_chiqish_soni = 0

while True:
    son = int(input())
    
    if son == 0:
        break
        
    if son < 2:
        continue
        
    # Tublikka tekshirish partiyasi
    tub = True
    i = 2
    while i * i <= son:
        if son % i == 0:
            tub = False
            break
        i += 1
        
    if tub:
        tub_chiqish_soni += 1
        
print(tub_chiqish_soni)