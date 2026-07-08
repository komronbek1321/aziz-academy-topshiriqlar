n = int(input())

ombor = {}
for _ in range(n):
    nomi, soni = input().split()
    ombor[nomi] = soni
    
qidirilgan_nom = input().strip()
print(ombor.get(qidirilgan_nom, "Topilmadi"))