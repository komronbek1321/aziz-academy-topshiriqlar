n = int(input())

talabalar = {}
for _ in range(n):
    ism, baho = input().split()
    talabalar[ism] = int(baho)
    
eng_yuqori_baho = -1
eng_yaxshi_talaba = ""

for ism, baho in sorted(talabalar.items()):
    if baho > eng_yuqori_baho:
        eng_yuqori_baho = baho
        eng_yaxshi_talaba = ism
        
print(f"{eng_yaxshi_talaba} {eng_yuqori_baho}")