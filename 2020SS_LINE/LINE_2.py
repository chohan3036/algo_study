import sys
from itertools import combinations
read = lambda: sys.stdin.readline().strip()


def solution(answer_sheet, sheets):
    ans = 0
    pairs = combinations(range(len(sheets)), 2)
    for first, second in pairs:
        sheet1, sheet2 = sheets[first], sheets[second]
        sus = 0
        cnt, max_cnt = 0, 0
        for i in range(len(answer_sheet)):
            if sheet1[i] == sheet2[i] != answer_sheet[i]:
                sus += 1
                cnt += 1
            else:
                if max_cnt < cnt:
                    max_cnt = cnt
                    cnt = 0
        result = sus + pow(max_cnt, 2)
        if ans < result:
            ans = result

    return ans


print(solution('53241', ['53241', '42133', '53241',
                              '14354']))
