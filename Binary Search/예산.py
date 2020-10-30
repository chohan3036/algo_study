def solution(budgets, M):
    start, end = 0, max(budgets)
    while start <= end:
        mid = (start + end) // 2
        _sum = sum([budget if budget <= mid else mid for budget in budgets])
        if _sum > M:
            end = mid - 1
        elif _sum < M:
            start = mid + 1
        else:
            return mid
    return (start + end) // 2