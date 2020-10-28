import sys
read = lambda: sys.stdin.readline().strip()


#n, d, k, c = map(int, read().split())
#susi = [int(read()) for _ in range(n)]
n, d, k, c = 8, 30, 4, 30
susi = [7, 9, 7, 30, 2, 7, 9, 25]

maxd = 1
can = []
for i in range(n - 4):
    can.append(set(susi[i: i + 4]))

print(maxd, can)
