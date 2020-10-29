import sys
read = lambda: sys.stdin.readline().strip()

#n, d, k, c = map(int, read().split())
#susi = [int(read()) for _ in range(n)]
n, d, k, c = 8, 30, 4, 30
susi = [12, 9, 7, 30, 2, 7, 9, 25]
susi += susi[: k - 1]

susi_list = []


print(susi_list)
ans = 1
coupon = 0
for susi in susi_list:
    if c not in susi:
        coupon = 1

print(ans + coupon)
