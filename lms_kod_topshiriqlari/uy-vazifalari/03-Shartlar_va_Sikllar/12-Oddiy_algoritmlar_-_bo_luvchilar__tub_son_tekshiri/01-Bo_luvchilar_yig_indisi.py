n = int(input())

divisors_sum = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisors_sum += i
print(divisors_sum)