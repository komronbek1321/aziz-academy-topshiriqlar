total = 0

while True:
    line = input().strip()
    if line == "stop":
        break
    total += int(line)
        
print(total)