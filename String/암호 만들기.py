import sys
read = lambda: sys.stdin.readline().strip()
from itertools import combinations

vowel = 'aeiou'

l, c = map(int, read().split())
chars = list(read().split())
chars.sort()

comb = combinations(chars, l)
for c in comb:
    vowel_cnt = 0
    for v in vowel:
        if v in c:
            vowel_cnt += 1
    if 0 < vowel_cnt < l - 1:
        print(''.join(c))
