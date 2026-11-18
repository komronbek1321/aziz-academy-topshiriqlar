n = int(input())
max_val = int(input())
max_pos = 1

for i in range(2, n + 1):
    x = int(input())
    if x > max_val:
        max_val = x
        max_pos = i
print(max_pos)