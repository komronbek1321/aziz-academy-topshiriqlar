n = int(input())

yigindi = 0
sanoq = 0

for _ in range(n):
    son = int(input())
    if son > 0:
        yigindi += son
        sanoq += 1
        
if sanoq > 0:
    print(yigindi // sanoq)
else:
    print(0)