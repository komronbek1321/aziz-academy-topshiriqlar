n = int(input())

topildi = False
i = 0

while i < n:
    son = int(input())
    i += 1
    
    if not topildi and son % 7 == 0:
        print(son)
        topildi = True
        break
        
if not topildi:
    print("yo'q")