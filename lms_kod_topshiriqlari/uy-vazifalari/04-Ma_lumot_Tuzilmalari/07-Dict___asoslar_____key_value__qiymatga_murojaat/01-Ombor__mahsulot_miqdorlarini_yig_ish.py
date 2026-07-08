n = int(input())

ombor = {}
tartib = []

for _ in range(n):
    satr = input().split()
    mahsulot = satr[0]
    miqdor = int(satr[1])
    
    if mahsulot in ombor:
        ombor[mahsulot] += miqdor
    else:
        ombor[mahsulot] = miqdor
        tartib.append(mahsulot)
        
for mahsulot in tartib:
    print(f"{mahsulot} {ombor[mahsulot]}")