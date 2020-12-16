notation = ['0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F']


def solution(n, t, m, p):
    all_num = ''
    for i in range(t * m):
        cur_num = ''
        while i >= n:
            cur_num = str(notation[i % n]) + cur_num
            i //= n
        cur_num = str(notation[i]) + cur_num
        all_num += cur_num

    ans = ''
    for i in range(t):
        ans += all_num[i * m + (p - 1)]
    return ans
