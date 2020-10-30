from collections import deque
import heapq
monthly = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]


def solution(n, customers):
    run = [0 for _ in range(n)]
    stop_time, start_time = [0 for _ in range(n)], [0 for _ in range(n)]
    realtime = 0

    ans = [0 for _ in range(n)]
    for customer in customers:
        date, time, task = map(str, customer.split())
        # 날짜 계산
        m, d = map(int, date.split('/'))
        date = monthly[m] + d
        # 시간 계산
        h, m, s = map(int, time.split(':'))
        time = h * 3600 + m * 60 + s
        # 운영되지 않은 시간을 구하기 위해
        # 실제 시각을 첫 손님의 도착시간으로 초기화
        if customer == customers[0]:
            realtime = time

        # 운영되지 않는 키오스크가 있다면
        # 운영되지 않은 시간이 가장 긴 것을 선택
        max_stop, chosen = 0, -1
        if 0 in run:
            for kiosk in run:
                if run[kiosk] == 0:
                    cur_stopped_time = realtime - stop_time[kiosk]
                    if cur_stopped_time > max_stop:
                        max_stop = cur_stopped_time
                        chosen = kiosk
                    # 시간이 같을 경우 고유시간이 더 앞인 걸 선택
                    elif cur_stopped_time == max_stop:
                        chosen = min(chosen, kiosk)

        # 모두 운영되고 있는 경우
        min_run = 0
        if chosen == -1:
            for kiosk in run:
                cur_running_time = start_time[kiosk] + task - realtime
                if cur_running_time < min_run:
                    min_run = cur_running_time
                    chosen = kiosk
                elif cur_running_time == min_run:
                    chosen = min(chosen, kiosk)

        run.append(chosen)
        realtime += 1

        ans[chosen] += 1
    return ans


print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26",
                   "10/01 23:31:00 05", "10/01 23:33:17 24",
                   "10/01 23:50:25 13", "10/01 23:55:45 20",
                   "10/01 23:59:39 03", "10/02 00:10:00 10"]))