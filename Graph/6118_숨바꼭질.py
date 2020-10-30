import sys
reading = lambda:sys.stdin.readline().strip()

N, M = map(int, reading().split())
cabins = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, reading().split())
    cabins[a].append(b)
    cabins[b].append(a)

visited = [0] * (N + 1)
d, now = 0, [1]
visited[1] = 1
while 1:
    nxt = []
    for i in now:
        for j in cabins[i]:
            if visited[j]:
                continue
            nxt.append(j)
            visited[j] = 1
    if nxt:
        now = nxt
        d += 1
    else:
        print(min(now), d, len(now))
        break
