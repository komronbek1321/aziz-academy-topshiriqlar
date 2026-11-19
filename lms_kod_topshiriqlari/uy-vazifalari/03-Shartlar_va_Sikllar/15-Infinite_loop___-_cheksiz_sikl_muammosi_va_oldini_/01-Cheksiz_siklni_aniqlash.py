start = int(input().strip())
step = int(input().strip())

if start >= 100:
  print(0)
elif step <= 0:
  print("CHEKSIZ")
else:
  steps = 0
  current = start
  while current < 100:
    current += step
    steps += 1
  print(steps)