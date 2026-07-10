n = int(input())
guruhlar = []

for _ in range(n):
    qator = input().split()
    guruh_nomi = qator[0]
    o_quvchilar = qator[1:]
    guruhlar.append({"nomi": guruh_nomi, "soni": len(o_quvchilar)})
    
for guruh in guruhlar:
    print(f"{guruh['nomi']} {guruh['soni']}")