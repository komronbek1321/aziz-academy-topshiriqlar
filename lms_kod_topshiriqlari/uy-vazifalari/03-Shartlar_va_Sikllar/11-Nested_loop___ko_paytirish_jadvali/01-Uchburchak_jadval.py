n = int(input())

for i in range(1, n + 1):
    qator = [str(i * j) for j in range(1, i + 1)]
    print(" ".join(qator))