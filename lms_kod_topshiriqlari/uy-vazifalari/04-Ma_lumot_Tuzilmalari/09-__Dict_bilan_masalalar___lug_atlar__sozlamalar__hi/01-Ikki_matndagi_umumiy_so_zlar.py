matn1 = input().split()
matn2 = input().split()

lugat = {}
for soz in matn1:
    lugat[soz] = True
    
umumiy = []
for soz in matn2:
    if soz in lugat and soz not in umumiy:
        umumiy.append(soz)
        
for soz in sorted(umumiy):
    print(soz)