n = int(input())
mahsulotlar = []

for _ in range(n):
    nomi, narxi = input().split()
    mahsulotlar.append({"nomi": nomi, "narxi": int(narxi)})
    
chegara = int(input())

for mahsulot in mahsulotlar:
    if mahsulot["narxi"] < chegara:
        print(mahsulot["nomi"])