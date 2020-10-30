n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start, end = 1, house[-1] - house[0]
ans = 0
while start <= end:
    mid = start + (start + end) // 2
    cnt = 1
    target = 0

    for i in range(n):
        if house[i] >= house[target] + mid:
            cnt += 1
            target = i

    if cnt >= c:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
