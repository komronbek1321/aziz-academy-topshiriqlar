n = int(input())
eng_yuqori_baho = -1
eng_yaxshi_o_quvchi = ""

for _ in range(n):
    qator = input().split()
    ism = qator[0]
    baholar = [int(b) for b in qator[1:]]
    
    if baholar:
        maks_baho = max(baholar)
        if maks_baho > eng_yuqori_baho:
            eng_yuqori_baho = maks_baho
            eng_yaxshi_o_quvchi = ism
            
print(f"{eng_yaxshi_o_quvchi} {eng_yuqori_baho}")