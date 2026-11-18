n = int(input())
yigindi = 0
soni = 0
for _ in range(n):
    x = int(input())
    if x > 0:
        yigindi += x
        soni += 1
        
if soni == 0:
    print(0)
else:
    print(yigindi // soni)