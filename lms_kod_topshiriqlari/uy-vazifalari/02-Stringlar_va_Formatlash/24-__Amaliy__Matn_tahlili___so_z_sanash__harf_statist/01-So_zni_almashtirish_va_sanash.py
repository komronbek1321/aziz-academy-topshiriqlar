matn = input()
soz = input()

almashtirilgan = matn.replace(soz, soz.upper())
soni = matn.count(soz)

print(almashtirilgan)
print(soni)