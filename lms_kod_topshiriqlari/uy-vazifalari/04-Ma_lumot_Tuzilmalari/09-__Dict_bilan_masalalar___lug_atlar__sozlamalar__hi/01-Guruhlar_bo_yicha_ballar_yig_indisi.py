n = int(input())

guruhlar = {}
for _ in range(n):
    guruh, ball = input().split()
    guruhlar[guruh] = guruhlar.get(guruh, 0) + int(ball)
    
for guruh in sorted(guruhlar.keys()):
    print(f"{guruh} {guruhlar[guruh]}")