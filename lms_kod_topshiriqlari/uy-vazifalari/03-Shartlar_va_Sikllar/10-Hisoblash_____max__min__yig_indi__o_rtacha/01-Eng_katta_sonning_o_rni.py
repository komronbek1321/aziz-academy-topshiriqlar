n = int(input())

eng_katta = int(input())
eng_katta_orin = 1

for i in range(2, n + 1):
    son = int(input())
    if son > eng_katta:
        eng_katta = son
        eng_katta_orin = i
print(eng_katta_orin)