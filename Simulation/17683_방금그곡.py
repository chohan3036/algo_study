prv = ['C#', 'D#', 'F#', 'G#', 'A#']
lat = ['c', 'd', 'f', 'g', 'a']


def solution(m, musicinfos):
    for i in range(len(prv)):
        m = m.replace(prv[i], lat[i])

    ans = []
    idx = 0
    for music in musicinfos:
        # 음악이 시작하고 끝난 시간, 제목, 악보를 , 기준으로 분리
        start, end, title, melody = map(str, music.split(','))
        for i in range(len(prv)):
            melody = melody.replace(prv[i], lat[i])

        # 음악이 재생된 시간을 구하기 위해 시간/분 단위로 분리해 계산
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = (end_h * 60 + end_m) - (start_h * 60 + start_m)

        # 재생시간이 악보 길이보다 길거나 짧을 때
        if time > len(melody):
            # 길면 처음부터 남은 시간만큼 다시 재생함
            melody = melody * (time // len(melody)) + melody[: time % len(melody)]

        # 짧으면 재생 시간만큼만 재생함
        elif time < len(melody):
            melody = melody[: time]

        # 처리된 음악이 네오가 기억한 멜로디와 같으면 제목 반환
        if m in melody:
            ans.append((time, idx, title))
            idx += 1

    if ans:
        ans = sorted(ans, key=lambda x: (x[0], -x[1]), reverse=True)
        return ans[0][2]
    else:
        return '(None)'


print(solution("CCB", ['03:00,03:28,FOO,CCB#CCB', '04:00,04:28,BAR,CCB#CCB']))
