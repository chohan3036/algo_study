import sys
read = lambda: sys.stdin.readline().strip()

str1, str2 = read(), read()
slen = len(str1)
dp = [[0 for _ in range(slen)] for _ in range(slen)]

for i in range(slen):
    for j in range(slen):
        if str1[i] == str2[j]:
            

print(dp)
