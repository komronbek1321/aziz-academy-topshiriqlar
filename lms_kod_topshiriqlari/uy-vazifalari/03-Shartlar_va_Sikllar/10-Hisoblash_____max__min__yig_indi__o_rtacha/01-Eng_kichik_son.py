n = int(input())
eng_kichik = int(input())
for i in range(n - 1):
    son = int(input())
    if son < eng_kichik:
        eng_kichik = son
print(eng_kichik)