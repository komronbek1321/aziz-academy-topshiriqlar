sonlar = list(map(int, input().split()))

sanoq = {}
for son in sonlar:
    sanoq[son] = sanoq.get(son, 0) + 1
    
moda = sonlar[0]
maks_takrorlanish = sanoq[moda]

for son in sanoq:
    if sanoq[son] > maks_takrorlanish:
        maks_takrorlanish = sanoq[son]
        moda = son
    elif sanoq[son] == maks_takrorlanish:
            if son < moda:
                moda = sonlar
print(moda)