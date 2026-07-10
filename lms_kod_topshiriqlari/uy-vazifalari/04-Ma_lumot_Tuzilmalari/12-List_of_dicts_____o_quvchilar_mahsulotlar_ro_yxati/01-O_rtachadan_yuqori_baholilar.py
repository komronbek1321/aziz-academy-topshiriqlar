n = int(input())
o_quvchilar = []

for _ in range(n):
    ism, baho = input().split()
    o_quvchilar.append({"ism": ism, "baho": int(baho)})
    
ortacha_baho = sum(oquvchi["baho"] for oquvchi in o_quvchilar) / n
for oquvchi in o_quvchilar:
    if oquvchi["baho"] > ortacha_baho:
        print(oquvchi["ism"])