import re

valid_passwords = "[Abc123@]"

items = [x.strip() for x in input("nhap mk: ").split(',')]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    if not re.search("[0-9]", p):
        continue
    if not re.search("[A-Z]", p):
        continue
    if not re.search("[$#@]", p):
        continue

    valid_passwords.append(p)

print(",".join(valid_passwords))
