n = input()
while len(n) > 1:
    s = 0
    for ch in n:
        s += int(ch)
    n = str(s)
print(n)