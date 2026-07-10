set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
set3 = set(map(int, input().split()))

kesishma = set1 & set2 & set3
saralangan_natija = sorted(kesishma)

print(*saralangan_natija)