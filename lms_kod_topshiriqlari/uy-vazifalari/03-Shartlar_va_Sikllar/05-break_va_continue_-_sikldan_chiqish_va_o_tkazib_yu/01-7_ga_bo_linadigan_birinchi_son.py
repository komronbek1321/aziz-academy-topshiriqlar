n = int(input().strip())
found = False
for _ in range(n):
    num = int(input().strip())
    if num % 7 == 0:
        print(num)
        found = True
        break
if not found:
    print("yo'q")
        