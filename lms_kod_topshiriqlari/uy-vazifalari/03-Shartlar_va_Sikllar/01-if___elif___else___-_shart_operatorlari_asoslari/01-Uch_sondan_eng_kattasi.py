a = int(input().strip())
b = int(input().strip())
c = int(input().strip())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)