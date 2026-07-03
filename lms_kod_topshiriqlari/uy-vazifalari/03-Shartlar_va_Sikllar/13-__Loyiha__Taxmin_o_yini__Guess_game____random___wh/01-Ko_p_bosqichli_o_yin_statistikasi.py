R = int(input())

jami_urinishlar = 0
eng_yaxshi_bosqich = float('inf')

for i in range(1, R + 1):
    yashirin = int(input())
    bosqich_urinishlari = 0
    
    while True:
        taxmin = int(input())
        bosqich_urinishlari += 1
        
        if taxmin == yashirin:
            break
            
    print(f"Round {i}: {bosqich_urinishlari} urinish")
    
    jami_urinishlar += bosqich_urinishlari
    if bosqich_urinishlari < eng_yaxshi_bosqich:
        eng_yaxshi_bosqich = bosqich_urinishlari
        
print(f"Jami: {jami_urinishlar}")
print(f"Eng yaxshi: {eng_yaxshi_bosqich}")