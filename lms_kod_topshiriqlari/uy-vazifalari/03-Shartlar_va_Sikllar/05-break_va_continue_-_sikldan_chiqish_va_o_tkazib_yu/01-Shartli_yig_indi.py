total = 0

while True:
    num = int(input().strip())
    if num == 0 or num > 100:
        break
    if num < 0:
        continue
    total += num
print(total) 