sonlar = set(input().split())
qidirilgan = input().strip()

if qidirilgan in sonlar:
    print("Bor")
else:
    print("Yo'q")