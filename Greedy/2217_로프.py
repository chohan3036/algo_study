import sys
readline = lambda: sys.stdin.readline().strip()

N = int(readline())
ropes = []
for _ in range(N):
    ropes.append(int(readline()))
ropes.sort()

_max = ropes[0] * N
for i in range(1, N):
    temp = ropes[i] * (N - i)
    if temp > _max:
        _max = temp

print(_max)
