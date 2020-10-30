dp = []
for _ in range(3):
    dp.append(1)

n = []
T = int(input())
for i in range(T):
    n.append(int(input()))

for i in range(3, max(n)):
    dp.append(dp[i-3] + dp[i-2])

for x in n:
    print(dp[x-1])


