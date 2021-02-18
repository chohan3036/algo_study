import sys
read = lambda: sys.stdin.readline().strip()

n = int(read())
liquids = list(map(int, read().split()))
liquids.sort()

if liquids[0] > 0:
    print(liquids[0], liquids[1])

else:
    left, right = 0, len(liquids) - 1
    ans = [liquids[left], liquids[right]]
    nearest = 2000000000
    while left < right:
        mix = liquids[left] + liquids[right]

        if mix == 0:
            ans = [liquids[left], liquids[right]]
            break

        if abs(nearest) > abs(mix):
            nearest = mix
            ans = [liquids[left], liquids[right]]

        if mix > 0:
            right -= 1
        else:
            left += 1

    print(ans[0], ans[1])
