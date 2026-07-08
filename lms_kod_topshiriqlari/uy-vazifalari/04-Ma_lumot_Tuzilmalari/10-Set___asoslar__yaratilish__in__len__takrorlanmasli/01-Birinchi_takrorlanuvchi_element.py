sonlar = input().split()

seen = set()
topildi = False

for son in sonlar:
    if son in seen:
        print(son)
        topildi = True
        break
    seen.add(son)
    
if not topildi:
    print("Yo'q")