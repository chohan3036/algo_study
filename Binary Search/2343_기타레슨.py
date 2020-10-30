n, m = map(int, input().split())
lessons = list(map(int, input().split()))

left, right = max(lessons), sum(lessons)
ans = right

while left <= right:
    mid = (left + right) // 2

    cnt, cur_bluray = 1, 0
    for lesson in lessons:
        cur_bluray += lesson
        if cur_bluray > mid:
            cnt += 1
            cur_bluray = lesson

    # cnt 가 주어진 블루레이 개수(m)보다 크거나 같으면
    # 블루레이의 크기가 더 커져야 함
    if cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        ans = min(ans, mid)

print(ans)
