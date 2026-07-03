yashirin = int(input())
ball = 100

while True:
    taxmin = int(input())
    
    if taxmin == yashirin:
        print("TOPDINGIZ")
        break
    elif taxmin > yashirin:
        print("KATTA")
        ball = max(0, ball - 10)
    else:
        print("KICHIK")
        ball = max(0, ball - 10)
        
print(f"Ball: {ball}")