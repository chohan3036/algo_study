# 이분탐색은 무엇을 찾아야 하는지, 무엇을 기준으로 할지,
# 최악의 경우를 알면 문제를 구현할 수 있어!!


def solution(n, times):
    left, right = 1, max(times) * n
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        cap = 0

        for t in times:
            cap += mid // t

            if cap >= n:
                ans = mid
                right = mid - 1
                break

        if cap < n:
            left = mid + 1

    return ans


print(solution(6, [7, 10]))
