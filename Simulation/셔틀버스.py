from collections import deque


def solution(n, t, m, timetable):
    # 시간 변환 및 정렬
    timetable = [int(time[: 2]) * 60 + int(time[3: ]) for time in timetable]
    timetable.sort()
    timeq = deque(timetable)

    # 이용 가능한 버스 목록
    busq = deque([[9 * 60 + t * i, m] for i in range(n)])

    # 대기자와 버스를 떠나는 순서대로 쌓음
    schedule = []
    while timeq or busq:
        # 대기자가 남았으면
        if timeq:
            cur_person = timeq[0]
        # 대기자가 없으면 남은 버스 뒤에 붙이고 break
        else:
            schedule.extend(busq)
            break

        # 버스가 남았으면
        if busq:
            cur_bus = busq[0]
        # 버스가 없으면 남은 대기자 뒤에 붙이고 break
        else:
            schedule.extend(timeq)
            break

        # 현재 대기자가 버스보다 빨리 와 있었으면
        # 버스에 타고 좌석 한 개 줄임
        if cur_person <= cur_bus[0]:
            schedule.append(timeq.popleft())
            cur_bus[1] -= 1
        # 버스보다 늦게 왔으면
        # 버스 떠남
        else:
            schedule.append(busq.popleft())

        # 버스 좌석이 다 차면
        # 버스 떠남
        if cur_bus[1] == 0:
            schedule.append(busq.popleft())

    for i in range(len(schedule) - 1, -1, -1):
        # 가장 마지막 버스를 기준으로
        if type(schedule[i]) is list:
            # 좌석이 남았으면
            # 마지막 버스에 탑승
            if schedule[i][1] > 0:
                return '{:02}:{:02}'.format(schedule[i][0] // 60, schedule[i][0] % 60)
            # 좌석이 없으면
            # 마지막 대기자 보다 1분 빨리 오기
            else:
                return '{:02}:{:02}'.format((schedule[i - 1] - 1) // 60, (schedule[i - 1] - 1) % 60)


print(solution(10, 60, 45, ['23:59','23:59','23:59','23:59',
                            '23:59','23:59','23:59','23:59',
                            '23:59','23:59','23:59','23:59',
                            '23:59','23:59','23:59','23:59',]))
