lst = []

while True:
    buyruq = input().split()
    amal = buyruq[0]
    
    
    if amal == "stop":
        break
    elif amal == "append":
            x = int(buyruq[1])
            lst.append(x)
    elif amal == "insert":
            i = int(buyruq[1])
            x = int(buyruq[2])
            lst.insert(i, x)
    elif amal == "remove":
            x = int(buyruq[1])
            if x in lst:
                lst.remove(x)
    elif amal == "pop":
                i = int(buyruq[1])
                lst.pop(i)
                
print(lst)