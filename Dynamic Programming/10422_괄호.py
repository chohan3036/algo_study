import sys
read = lambda: sys.stdin.readline().strip()

MOD = 1000000007
d = [0] * 5001
d[0] = 1
for i in range(2, 5001, 2):
    for j in range(2, i + 1, 2):
        d[i] += d[j - 2] * d[i - j]

t = int(read())
for _ in range(t):
    l = int(read())
    print(d[l] % MOD)
