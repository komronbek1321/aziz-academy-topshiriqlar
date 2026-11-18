target = int(input())
ball = 100
while True:
    guess = int(input())
    if guess > target:
        print("KATTA")
        ball = max(0, ball - 10)
    elif guess < target:
        print("KICHIK")
        ball = max(0, ball - 10)
    else:
        print("TOPDINGIZ")
        print(f"Ball: {ball}")
        break