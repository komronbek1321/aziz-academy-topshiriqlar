n = int(input())
eng_kop_guruh = ""
maks_soni = -1

for _ in range(n):
    qator = input().split()
    guruh_nomi = qator[0]
    a_zolar_soni = len(qator[1:])
    
    if a_zolar_soni > maks_soni:
        maks_soni = a_zolar_soni
        eng_kop_guruh = guruh_nomi
        
print(eng_kop_guruh)