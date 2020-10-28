import sys
read = lambda: sys.stdin.readline()

n, c = map(int, read().split())
houses = [int(read()) for _ in range(n)]
houses.sort()

ans = 0
# 최소는 1, 최대는 가장 멀리 있는 집(또는 멀리 있는 집 - 가까이 있는 집)
left, right = 1, houses[-1] - houses[0]

# 이분탐색
while left <= right:
    mid = (left + right) // 2

    # 맨 처음 공유기를 설치한 집
    target = 0
    # 공유기 개수
    router_cnt = 1

    for i in range(n):
        # 공유기를 설치해 놓은 집과 거리를 재가면서
        # mid 보다 큰 경우에만 설치하고 그 집을 다시 target 으로 설정
        # 인접한 '최대' 거리를 알고 싶은 거니까!!
        if houses[i] - houses[target] >= mid:
            router_cnt += 1
            target = i

    # 주어진 공유기와 개수가 같더라도 최대를 찾기 위해 = 포함함
    if router_cnt >= c:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)
