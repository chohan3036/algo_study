import sys
read = lambda: sys.stdin.readline().strip()

for _ in range(int(read())):
    n, m = map(int, read().split())
    a = list(map(int, read().split()))
    b = list(map(int, read().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    alen, blen = len(a), len(b)
    i = j = 0
    ans = 0
    while i < alen and j < blen:
        if a[i] > b[j]:
            ans += blen - j
            i += 1
        else:
            j += 1

    print(ans)
