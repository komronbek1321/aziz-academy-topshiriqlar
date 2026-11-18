email = input()
parol = input()

shart = ('@' in email and '.' in email and 8 <= len(parol) <= 16 and email == email.lower())
print(str(shart))