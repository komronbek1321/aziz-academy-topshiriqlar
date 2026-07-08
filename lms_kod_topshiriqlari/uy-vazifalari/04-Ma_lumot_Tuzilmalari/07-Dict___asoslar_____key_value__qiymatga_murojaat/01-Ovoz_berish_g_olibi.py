n = int(input())

ovozlar = {}
tartib = []

for _ in range(n):
    nomzod = input().strip()
    if nomzod in ovozlar:
        ovozlar[nomzod] += 1
    else:
        ovozlar[nomzod] = 1
        tartib.append(nomzod)
        
golib = tartib[0]
maks_ovoz = ovozlar[golib]

for nomzod in tartib:
    if ovozlar[nomzod] > maks_ovoz:
        maks_ovoz = ovozlar[nomzod]
        golib = nomzod
        
print(golib)