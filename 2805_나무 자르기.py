import sys
read = lambda: sys.stdin.readline().strip()


def bin_search(target, array):
    ans = 0
    left, right = 0, array[-1]
    while left <= right:
        mid = (left + right) // 2

        collected = 0
        for a in array:
            if a > mid:
                collected += a - mid

        if target <= collected:
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1

    return ans


n, m = map(int, read().split())
trees = list(map(int, read().split()))
trees.sort()

print(bin_search(m, trees))
