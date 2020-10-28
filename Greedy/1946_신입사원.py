# input 쓰면 시간초과
import sys
read = lambda : sys.stdin.readline().strip()

t = int(read())
for _ in range(t):
    n = int(read())
    candidates = [tuple(map(int, read().split())) for _ in range(n)]
    candidates.sort(key=lambda x: x[0])

    cnt = 1
    _min = candidates[0][1]

    for i in range(1, n):
        if candidates[i][1] < _min:
            _min = candidates[i][1]
            cnt += 1

    print(cnt)
