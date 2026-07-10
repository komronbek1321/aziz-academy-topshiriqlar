n = int(input())
guruhlar = {}

for _ in range(n):
    qator = input().split()
    guruh_nomi = qator[0]
    o_quvchilar = qator[1:]
    guruhlar[guruh_nomi] = o_quvchilar
    
qidiruv_guruhi, qidiruv_ismi = input().split()

if qidiruv_ismi in guruhlar[qidiruv_guruhi]:
    print("Ha")
else:
    print("Yoq")