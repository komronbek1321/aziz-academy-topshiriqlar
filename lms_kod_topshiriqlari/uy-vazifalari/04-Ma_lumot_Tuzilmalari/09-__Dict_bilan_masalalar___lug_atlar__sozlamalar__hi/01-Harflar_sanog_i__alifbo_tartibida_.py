soz = input().strip()

sanoq = {}
for harf in soz:
    sanoq[harf] = sanoq.get(harf, 0) + 1
    
for harf in sorted(sanoq.keys()):
    print(f"{harf} {sanoq[harf]}")