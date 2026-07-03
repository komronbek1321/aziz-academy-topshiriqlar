login = input()
parol = input()

shart1 = len(login) >= 3
shart2 = len(parol) >= 8
shart3 = login != parol

print(shart1 and shart2 and shart3)