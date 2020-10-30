import sys
readline = lambda:sys.stdin.readline().strip()

T = int(readline())
for _ in range(T):
    n, m = map(int, readline().split())
    R = [0 for _ in range(n)]
    C = []
    for _ in range(m):
        x, y = map(int, readline().split())
        C.append((x, y))
    C.sort()

def color():
    R[0] = 1
    for c in C:
        a, b = c



