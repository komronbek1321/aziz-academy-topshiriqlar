count = int(input())
price = int(input())
discount_percent = int(input())

total_sum = count * price
discount_amount = (total_sum * discount_percent) // 100
final_sum = total_sum - discount_amount

print(total_sum)
print(discount_amount)
print(final_sum)