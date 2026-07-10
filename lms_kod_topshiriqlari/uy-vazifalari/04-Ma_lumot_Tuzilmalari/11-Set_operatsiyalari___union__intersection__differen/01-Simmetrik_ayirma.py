set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
simmetrik = set1 ^ set2
saralangan_natija = sorted(simmetrik)
print(*saralangan_natija)