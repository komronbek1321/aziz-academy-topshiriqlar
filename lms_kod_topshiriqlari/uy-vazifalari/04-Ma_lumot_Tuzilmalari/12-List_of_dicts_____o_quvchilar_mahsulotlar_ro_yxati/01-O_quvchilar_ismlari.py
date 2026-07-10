n = int(input())
o_quvchilar = []

for _ in range(n):
    ism, yosh = input().split()
    o_quvchilar.append({"ism": ism, "yosh": int(yosh)})
    
for oquvchi in o_quvchilar:
    print(oquvchi["ism"])