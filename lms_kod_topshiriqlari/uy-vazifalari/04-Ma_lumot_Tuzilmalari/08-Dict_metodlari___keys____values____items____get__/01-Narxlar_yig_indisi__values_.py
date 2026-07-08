n = int(input())

mahsulotlar = {}
for _ in range(n):
    nomi, narxi = input().split()
    mahsulotlar[nomi] = int(narxi)
    
print(sum(mahsulotlar.values()))