# 이분탐색..?


def time_to_time(string):
    time = list(string.split(':'))
    time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    return time


def solution(play_time, adv_time, logs):
    # 영상 시간과 광고 시간의 길이가 같을 경우
    if play_time == adv_time:
        return '00:00:00'

    adv_time = time_to_time(adv_time)

    timeline = []
    idx = 0
    for log in logs:
        log = list(log.split('-'))
        timeline.append((time_to_time(log[0]), time_to_time(log[1]), idx))
        idx += 1

    flag_cnt = [[0, 0, 0] for _ in range(len(timeline))]
    for i in range(len(timeline)):
        flag_cnt[i][1] = timeline[i][0]
        flag_cnt[i][2] = i
        for times in timeline:
            if times[0] <= timeline[i][0] + adv_time <= times[1]:
                flag_cnt[i][0] += 1

    flag_cnt = sorted(flag_cnt, key=lambda x: (x[0], -x[1]), reverse=True)
    ans = logs[flag_cnt[0][2]].split('-')[0]

    return ans


print(solution("99:59:59", "25:00:00",
               ["69:59:59-89:59:59", "01:00:00-21:00:00",
                "79:59:59-99:59:59", "11:00:00-31:00:00"]))
