n = int(input())

talabalar = {}
for _ in range(n):
    ism, baho = input().split()
    talabalar[ism] = int(baho)
    
reyting = sorted(talabalar.items(), key=lambda x: (-x[1], x[0]))

for ism, baho in reyting:
    print(f"{ism} {baho}")