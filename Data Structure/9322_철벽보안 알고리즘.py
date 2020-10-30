import sys
readin = lambda: sys.stdin.readline().strip()

N = int(readin())
for i in range(N):
    n = int(readin())
    s = []
    for j in range(3):
        s.append(readin().split())
    s_num = []
    for k in range(n):
        s_num.append(s[1].index(s[0][k]))
    for n in s_num:
        print(s[2][n], end=' ')
