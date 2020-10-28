import sys
read = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(read())
    liquids = list(map(int, read().split()))

    liquids.sort()
    if liquids[0] > 0:
        print(liquids[0], liquids[1])

    else:
        i, j = 0, len(liquids) - 1
        near0 = 2000000000
        ans = [liquids[i], liquids[j]]
        while i < j:
            cur_liquid = liquids[i] + liquids[j]

            if cur_liquid == 0:
                near0 = 0
                ans[0], ans[1] = liquids[i], liquids[j]
                break

            if abs(near0) > abs(cur_liquid):
                near0 = cur_liquid
                ans[0], ans[1] = liquids[i], liquids[j]

            if cur_liquid > 0:
                j -= 1

            else:
                i += 1

        ans.sort()
        print(ans[0], ans[1])
