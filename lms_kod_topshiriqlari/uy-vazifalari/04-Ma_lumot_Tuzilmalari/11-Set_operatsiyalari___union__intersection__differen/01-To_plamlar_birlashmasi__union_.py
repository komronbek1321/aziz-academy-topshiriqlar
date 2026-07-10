set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
birlashma = set1 | set2
saralangan_natija = sorted(birlashma)
print(*saralangan_natija)