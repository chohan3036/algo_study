import sys
read = lambda: sys.stdin.readline()


def ok(a, b, op):
    if op == '>':
        if not a > b:
            return False
    else:
        if not a < b:
            return False
    return True


def go(idx, choose):
    if idx == k + 1:
        ans.append(choose)
        return

    for i in range(10):
        if check[i]:
            continue
        if idx == 0 or ok(int(choose[idx - 1]), i, sign[idx - 1]):
            check[i] = 1
            go(idx + 1, choose + str(i))
            check[i] = 0


k = int(read())
sign = list(map(str, read().split()))
ans = []
check = [0 for _ in range(10)]
go(0, '')
print(ans[-1])
print(ans[0])
