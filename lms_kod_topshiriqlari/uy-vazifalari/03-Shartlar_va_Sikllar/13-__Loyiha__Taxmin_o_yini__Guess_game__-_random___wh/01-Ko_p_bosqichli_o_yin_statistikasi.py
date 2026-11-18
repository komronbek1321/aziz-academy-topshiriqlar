r = int(input())
total_ur = 0
min_ur = float('inf')

for i in range(1, r + 1):
    target = int(input())
    ur = 0
    while True:
        guess = int(input())
        ur += 1
        if guess == target:
            break
    print(f"Round {i}: {ur} urinish")
    total_ur += ur
    if ur < min_ur:
        min_ur = ur
print(f"Jami: {total_ur}")
print(f"Eng yaxshi: {min_ur}")