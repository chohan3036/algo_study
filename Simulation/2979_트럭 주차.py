from collections import Counter
MAX = 101

costs = list(map(int, input().split()))

time = [0 for _ in range(MAX)]
for _ in range(3):
    arr, dep = map(int, input().split())
    for i in range(arr + 1, dep + 1):
        time[i] += 1

bill = Counter(time)
bill = sorted(bill.items(), key=lambda x: x[0])

ans = 0
for b in bill:
    if b[0] == 0:
        continue
    else:
        ans += b[0] * b[1] * costs[b[0] - 1]

print(ans)
