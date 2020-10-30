t = int(input())
for test in range(t):
    n = int(input())
    price = list(map(int, input().split()))

    start, end = 0, n - 1
    profit = 0

    while start <= end:
        pay, cnt = 0, 0

        max_idx = price[start:].index(max(price[start:])) + start
        if max_idx == start:
            start += 1
            continue

        for i in range(start, max_idx):
            pay += price[i]
            cnt += 1
        profit += price[max_idx] * cnt - pay
        start = max_idx + 1

    print(''.join(('#', str(test + 1))), profit)
