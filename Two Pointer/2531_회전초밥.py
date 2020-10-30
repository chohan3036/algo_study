import sys
read = lambda: sys.stdin.readline().strip()
from collections import deque

#n, d, k, c = map(int, read().split())
#susi = [int(read()) for _ in range(n)]
n, d, k, c = 8, 30, 4, 30
susi = [12, 9, 7, 30, 2, 7, 9, 25]
susi += susi[: k - 1]

susi_window = deque([])
stt, cnt = 0, 0
ans = 0
for end in range(n + k - 1):
    if susi[end] not in susi_window:
        cnt += 1
    susi_window.append(susi[end])

    if end >= k - 1:
        flag = False
        if c not in susi_window:
            ans = max(ans, cnt + 1)
        else:
            ans = max(ans, cnt)
        if susi_window.popleft() not in susi_window:
            cnt -= 1
        stt += 1

print(ans)
