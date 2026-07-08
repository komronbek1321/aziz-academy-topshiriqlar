n = int(input())

lugat = {}
for _ in range(n):
    ism, baho = input().split()
    lugat[ism] = baho
    
print(*(sorted(lugat.keys())))