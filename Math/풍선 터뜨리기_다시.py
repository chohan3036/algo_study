def solution(a):
    length = len(a)

    mins = [[0 for _ in range(length)] for _ in range(2)]
    left_min, right_min = a[0], a[-1]
    mins[0][0], mins[1][-1] = left_min, right_min

    for i in range(1, length):
        left_min = min(left_min, a[i])
        mins[0][i] = left_min

    for i in range(length - 1, -1, -1):
        right_min = min(right_min, a[i])
        mins[1][i] = right_min

    ans = 0
    for i in range(length):
        if a[i] > mins[0][i] and a[i] > mins[1][i]:
            continue
        ans += 1

    return ans


print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
