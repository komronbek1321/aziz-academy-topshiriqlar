secret = int(input())
attempts = 0

while True:
    guess = int(input())
    attempts += 1
    
    if guess > secret:
        print("KATTA")
    elif guess < secret:
        print("KICHIK")
    else:
        print("TOPDINGIZ")
        break
print(f"Urinishlar: {attempts}")