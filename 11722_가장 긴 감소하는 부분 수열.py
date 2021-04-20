# n = int(input())
# a = list(map(int, input().split()))
#
# dp = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if a[i] < a[j]:
#             dp[i] = max(dp[j] + 1, dp[i])
#
# print(max(dp))
from bisect import bisect_left

n = int(input())
a = list(map(lambda x: int(x) * -1, input().split()))

dp = [a[0]]

for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect_left(dp, a[i])
        dp[idx] = a[i]

print(len(dp))
