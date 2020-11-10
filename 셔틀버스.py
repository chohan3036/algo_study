from collections import deque


def solution(n, t, m, timetable):
    # 시간 변환 및 정렬
    new_times = []
    for time in timetable:
        hh, mm = map(int, time.split(':'))
        new_times.append(hh * 60 + mm)
    new_times.sort()

    # 이용 가능한 버스 목록
    shuttle = []
    last_bus = 0
    for i in range(n):
        shuttle.append(540 + t * i)
    print(shuttle)

    total = n * m
    for i in range(len(new_times)):
        if new_times[i] <= last_bus:
            total -= 1

        if total <= 0:
            h, m = (new_times[i] - 1) // 60, (new_times[i] - 1) % 60
            if m < 10:
                return '0' + str(h) + ':0' + str(m)
            else:
                return '0' + str(h) + ':' + str(m)

    h, m = last_bus // 60, last_bus % 60
    if m < 10:
        return '0' + str(h) + ':0' + str(m)
    else:
        return '0' + str(h) + ':' + str(m)


print(solution(2, 10, 2, ['09:10', '09:09', '08:00']))
