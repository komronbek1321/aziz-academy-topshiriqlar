n = int(input())
jami_o_quvchilar = 0

for _ in range(n):
    qator = input().split()
    o_quvchilar = qator[1:]
    jami_o_quvchilar += len(o_quvchilar)
    
print(jami_o_quvchilar)