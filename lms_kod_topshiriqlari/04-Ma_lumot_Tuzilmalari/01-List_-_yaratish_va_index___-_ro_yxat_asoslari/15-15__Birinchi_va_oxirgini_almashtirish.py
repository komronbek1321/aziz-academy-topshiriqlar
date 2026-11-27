n = int(input())
sonlar = list(map(int, input().split()))

sonlar[0], sonlar[-1] = sonlar[-1], sonlar[0]

print(sonlar)