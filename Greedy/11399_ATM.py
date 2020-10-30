import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split(' ')))
P.sort()
add = 0
all = 0
for i in P:
    add += i
    all += add
print(all)
