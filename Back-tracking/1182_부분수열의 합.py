import sys
readline = lambda :sys.stdin.readline().strip()

N, S = map(int, readline().split())
mat = list(map(int, readline().split()))
cnt = 0


def dfs(idx, sum_value):
    global cnt
    if idx >= N:
        if sum_value == S:
            cnt += 1
        return
    dfs(idx + 1, sum_value + mat[idx])
    dfs(idx + 1, sum_value)

dfs(0, 0)
print(cnt if S else cnt-1)