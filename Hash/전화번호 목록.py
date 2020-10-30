phone_book = ['123','456','789','78']

flag = True
for i, p in enumerate(phone_book):
    for j in range(len(phone_book)):
        if i == j:
            continue
        l = len(p)
        if p == phone_book[j][: l]:
            flag = False
            break
    if not flag:
        break

print(flag)

'''
from collections import Counter

ans = True
hash_map = Counter(phone_book)
for phone_number in hash_map:
    tmp = ''
    for number in phone_number:
        tmp += number
        if tmp in hash_map and tmp != phone_number:
            ans = False
            break
    if not ans:
        break

print(ans)
'''
