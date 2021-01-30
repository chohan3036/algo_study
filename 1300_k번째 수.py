# 이분 탐색 - 임의의 충분히 큰 수 x를 이용한다.
# x는 k번째 숫자를 포함하므로

n = int(input())
k = int(input())

ans = 0
left, right = 1, k
while left <= right:
    cnt = 0
    mid = (left + right) // 2

    for i in range(1, n + 1):
        cnt += min(mid // i, n)

    if cnt < k:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)
