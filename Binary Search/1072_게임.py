from math import floor

x, y = map(int, input().split())
prev_z = int(y * 100 / x)

if prev_z >= 99:
    print(-1)

else:
    left, right = 0, 10000000000
    while left <= right:
        mid = (left + right) // 2
        z = floor((y + mid) * 100 / (x + mid))

        if z > prev_z:
            right = mid - 1
        else:
            left = mid + 1

    print(right + 1)
