# SW EXPERT ACADEMY
def dfs(num, depth):
    global ans

    int_num = int(''.join(map(str, num)))

    if depth == cnt:
        if int_num > ans:
            ans = int_num
        return

    if max_num[depth] >= int_num:
        return

    max_num[depth] = int_num

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            dfs(num, depth + 1)
            num[i], num[j] = num[j], num[i]


n = int(input())
for i in range(n):
    num, cnt = map(str, input().split())
    num = list(num)
    cnt = int(cnt)
    max_num = [-1] * 10
    ans = 0
    dfs(num, 0)
    print(''.join(('#', str(i + 1))), ans)
