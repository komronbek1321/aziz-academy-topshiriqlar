soz = input().strip()

chastota = {}
for harf in soz:
    if harf in chastota:
        chastota[harf] += 1
    else:
        chastota[harf] = 1
        
for harf, soni in chastota.items():
    print(f"{harf} {soni}")