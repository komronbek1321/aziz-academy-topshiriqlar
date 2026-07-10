n = int(input())
o_quvchilar = []

for _ in range(n):
    ism, yosh = input().split()
    o_quvchilar.append({"ism": ism, "yosh": int(yosh)})
    
eng_katta = max(o_quvchilar, key=lambda x: x["yosh"])
print(eng_katta["ism"])