n = int(input())
o_quvchilar = []

for _ in range(n):
    ism, mat, fiz = input().split()
    o_quvchilar.append({"ism": ism, "mat": int(mat), "fiz": int(fiz)})
    
for oquvchi in o_quvchilar:
    jami_ball = oquvchi["mat"] + oquvchi["fiz"]
    print(oquvchi["ism"], jami_ball)