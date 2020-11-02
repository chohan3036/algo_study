import sys
read = lambda: sys.stdin.readline().strip()

str1, str2 = read(), read()
dp1, dp2 = [0] * len(str1), [0] * len(str2)

for i in range(len(str1)):
    if str1[i] == str2[i]:

