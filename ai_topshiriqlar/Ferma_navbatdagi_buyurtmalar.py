# Ferma: navbatdagi buyurtmalar
# Kurs: Dasturlash / IT
# Mavzu: Dasturlashga kirish — Python nima va nega o'rganamiz
# Ball: 100
# Aziz Academy — AI Topshiriq

# Yechimingizni shu yerga yozing
# Kirish: input(), chiqish: print()
n = int(input())

limit = 100000
jami_summa = 0
qabul_qilinganlar = 0
rad_etildi = False

for _ in range(n):
    val = int(input())
    if not rad_etildi and jami_summa + val <= limit:
        jami_summa += val
        qabul_qilinganlar += 1
    else:
        rad_etildi = True
        
qolganlar = n - qabul_qilinganlar

print(qabul_qilinganlar)
print(jami_summa)
print(qolganlar)