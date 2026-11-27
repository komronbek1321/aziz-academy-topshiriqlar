n = int(input())
qismlar = input().split()
lst = []

for x in qismlar:
    lst.insert(0, int(x))
    
print(lst)