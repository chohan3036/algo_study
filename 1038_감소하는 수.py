n = int(input())
dp = [i for i in range(10)]

cnt, idx = 0, 1
flag = False

while cnt <= n - 10:
    if idx >= 1023:
        cnt += 1
        dp.append(-1)
    else:
        for i in range(int(str(dp[idx])[-1:])):
            cnt += 1
            dp.append(int(str(dp[idx]) + str(i)))

        idx += 1

print(dp[n])
