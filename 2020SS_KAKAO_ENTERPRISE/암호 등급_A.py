import sys
read = lambda: sys.stdin.readline().strip()

password = read()
level = 0
lower, upper, nat, spc, length = False, False, False, False, False
spc_words = '!@#$%^&*()`~-_=+,./<>?[]{}\|'

for i in range(len(password)):
    if not lower and password[i].islower():
        lower = True
        level += 1

    if not upper and password[i].isupper():
        upper = True
        level += 1

    if not nat and password[i].isdigit() and 0 <= int(password[i]) <= 9:
        nat = True
        level += 1

    if not spc and password[i] in spc_words:
        spc = True
        level += 1

    if not length and len(password[: i + 1]) >= 10:
        length = True
        level += 1

print(''.join(['LEVEL', str(level)]))
