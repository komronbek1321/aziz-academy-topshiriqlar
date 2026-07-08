n = int(input())

baholar = {}
for _ in range(n):
    ism, baho = input().split()
    baholar[ism] = baho
qidirilgan_ism = input().strip()
print(baholar[qidirilgan_ism])