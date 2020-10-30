import sys

def dfs(i, j):
    if i >= N or j >= N or i < 0 or j <0:
        return
    if L[i][j] == 0:
        return

    L[i][j] = 0
    num[n] += 1
    dfs(i, j-1)
    dfs(i, j+1)
    dfs(i-1, j)
    dfs(i+1, j)

N = int(sys.stdin.readline())
L = []
for i in range(N):
    L.append([])
    temp = sys.stdin.readline()
    for j in range(N):
        L[i].append(int(temp[j]))

num = [0]
n = 0

for i in range(N):
    for j in range(N):
        if L[i][j] == 1:
            num.append(0)
            n += 1
            dfs(i, j)

num.sort()
print(n)
for i in range(1, n+1):
    print(num[i])