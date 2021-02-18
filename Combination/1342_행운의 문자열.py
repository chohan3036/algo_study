import sys
read = lambda: sys.stdin.readline().strip()
from itertools import permutations
from collections import Counter
import math

s = read()
perm = permutations(sorted(s), len(s))
ans = 0
for p in perm:
    flag = True
    for i in range(1, len(p)):
        if p[i - 1] == p[i]:
            flag = False
            break
    if flag:
        ans += 1

counter = Counter(s)
for key in counter:
    ans //= math.factorial(counter[key])

print(ans)
