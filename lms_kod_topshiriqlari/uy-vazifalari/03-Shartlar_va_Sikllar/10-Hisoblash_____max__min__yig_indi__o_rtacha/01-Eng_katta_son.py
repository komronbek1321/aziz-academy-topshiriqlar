n = int(input())
eng_katta = int(input())
for i in range(n - 1):
    son = int(input())
    if son > eng_katta:
        eng_katta = son
print(eng_katta)