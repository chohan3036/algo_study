import sys
from collections import Counter
input = lambda: sys.stdin.readline().strip()

x = input()
y = input()
a = Counter(x)
b = Counter(y)

for i in b.keys():
    if a[i] < b[i]:
        print(0)
        break
else:
    print(int(y in x))