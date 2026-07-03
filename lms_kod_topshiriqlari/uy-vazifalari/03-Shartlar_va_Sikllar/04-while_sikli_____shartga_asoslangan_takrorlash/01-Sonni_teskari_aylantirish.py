n = int(input())

teskari = 0

while n > 0:
    qoldiq = n % 10
    teskari = teskari * 10 + qoldiq
    n = n // 10
    
print(teskari)