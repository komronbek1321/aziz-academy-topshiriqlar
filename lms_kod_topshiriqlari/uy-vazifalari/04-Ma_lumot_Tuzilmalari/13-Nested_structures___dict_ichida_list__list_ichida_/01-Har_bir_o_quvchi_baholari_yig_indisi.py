n = int(input())
o_quvchilar = []

for _ in range(n):
    qator = input().split()
    ism = qator[0]
    baholar = [int(b) for b in qator[1:]]
    o_quvchilar.append({"ism": ism, "baholar": baholar})
    
for oquvchi in o_quvchilar:
    print(f"{oquvchi['ism']} {sum(oquvchi['baholar'])}")