from math import ceil


def solution(progresses, speeds):
    ans = []
    days = [0 for _ in range(len(progresses))]
    cnt = 1
    for i in range(len(days)):
        days[i] = ceil((100 - progresses[i]) / speeds[i])
        if i == 0:
            cur_day = days[i]
            continue
        elif days[i] <= cur_day:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            cur_day = days[i]
    ans.append(cnt)
    return ans


print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]))
