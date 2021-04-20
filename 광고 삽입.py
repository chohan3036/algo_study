def time_to_sec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def sec_to_time(time):
    h = time // 3600
    time %= 3600
    m = time // 60
    time %= 60

    h = str(h) if h > 9 else str(0) + str(h)
    m = str(m) if m > 9 else str(0) + str(m)
    time = str(time) if time > 9 else str(0) + str(time)
    return ''.join([h, ':', m, ':', time])


def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)
    timeline = [0] * (play_sec + 1)

    for log in logs:
        start, end = time_to_sec(log.split('-')[0]), time_to_sec(log.split('-')[1])
        timeline[start] += 1
        timeline[end] -= 1

    for i in range(1, play_sec + 1):
        timeline[i] += timeline[i - 1]

    # for i in range(1, play_sec + 1):
    #     timeline[i] += timeline[i - 1]

    ans = 0
    max_play = sum(timeline[: adv_sec])
    prev_play = max_play
    for i in range(1, play_sec + 1):
        if i + adv_sec > play_sec:
            break
        cur_play = prev_play - timeline[i - 1] + timeline[i + adv_sec]
        if cur_play > max_play:
            max_play = cur_play
            ans = i
        prev_play = cur_play

    return sec_to_time(ans)


print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59",
                                        "01:00:00-21:00:00",
                                        "79:59:59-99:59:59",
                                        "11:00:00-31:00:00"]))
