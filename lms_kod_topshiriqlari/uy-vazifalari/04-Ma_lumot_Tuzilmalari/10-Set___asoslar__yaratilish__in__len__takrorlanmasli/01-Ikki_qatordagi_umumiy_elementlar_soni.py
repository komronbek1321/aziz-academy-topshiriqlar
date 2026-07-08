set1 = set(input().split())
set2 = set(input().split())

sanoq = 0
for element in set1:
    if element in set2:
        sanoq += 1
        
print(sanoq)