secret = int(input())
n = int(input())

found = False
for _ in range(n):
    guess = int(input())
    if guess < secret:
        print("KICHIK")
    elif guess > secret:
        print("KATTA")
    else:
        print("TOPDINGIZ")
        found = True
        break
if not found:
    print("YUTQAZDINGIZ")