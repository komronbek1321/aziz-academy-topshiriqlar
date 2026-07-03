n = int(input())

tub_sonlar = []

for i in range(2, n + 1):
    tub = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            tub = False
            break
    if tub:
        tub_sonlar.append(str(i))
        
print(" ".join(tub_sonlar))