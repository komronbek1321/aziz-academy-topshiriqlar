yashirin = int(input())
k = int(input())

for _ in range(k):
    taxmin = int(input())
    
    if taxmin == yashirin:
        print("TOPDINGIZ")
    elif taxmin > yashirin:
        print("KATTA")
    else:
        print("KICHIK")