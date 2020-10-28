import sys
sys.setrecursionlimit(10**9)


def moo(k):
    if k <= 3:
        if k == 1:
            return "m"
        else:
            return "0"

    return


n = int(input())
moo_len = [0 for _ in range(n)]
moo_len[0] = 3
for i in range(1, n):
    moo_len[i] = 2 * moo_len[i - 1] + i + 3
sn = moo(n)
print(moo_len[n - 1])
