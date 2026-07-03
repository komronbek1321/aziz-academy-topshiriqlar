yashirin = int(input())
urinishlar = 0

while True:
    taxmin = int(input())
    urinishlar += 1
    
    if taxmin == yashirin:
        print("TOPDINGIZ")
        break
    elif taxmin > yashirin:
        print("KATTA")
    else:
        print("KICHIK")
        
print(f"Urinishlar: {urinishlar}")