n = int(input())

positive_sum = 0
for _ in range(n):
    x = int(input())
    if x > 0:
        positive_sum += x
        
print(positive_sum)