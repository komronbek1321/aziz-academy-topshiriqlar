set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
ayirma = set1 - set2
saralangan_natija = sorted(ayirma)
print(*saralangan_natija)