import sys
reading = lambda :sys.stdin.readline().strip()

N, K = map(int, reading().split())
capacity = [-1 for _ in range(K + 1)]
capacity[0] = 0

for i in range(N):
    w, v = map(int, reading().split())
    for j in range(K - w, -1, -1):
        if capacity[j] == -1:
            continue
        capacity[j + w] = max(capacity[j + w], capacity[j] + v)
print(max(capacity))