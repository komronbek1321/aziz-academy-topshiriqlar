yashirin = int(input())
n = int(input())

topdi = False

for _ in range(n):
    taxmin = int(input())
    
    if taxmin == yashirin:
        print("TOPDINGIZ")
        topdi = True
        break
    elif taxmin > yashirin:
        print("KATTA")
    else:
        print("KICHIK")
        
if not topdi:
    print("YUTQAZDINGIZ")