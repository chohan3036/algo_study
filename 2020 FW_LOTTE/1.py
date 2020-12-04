def solution(votes):
    # 득표 수의 빈도를 담을 리스트
    vote_cnt = [0 for _ in range(1001)]

    # 투표 항목을 탐색하며 득표 수 빈도를 저장
    for vote in votes:
        vote_cnt[vote] += 1

    # 득표 수 빈도가 1보다 크면 = 유일하지 않으면
    # 해당 항목에 투표함
    ans = 0
    for vote in votes:
        if vote_cnt[vote] > 1:
            vote_cnt[vote] -= 1
            vote_cnt[vote + 1] += 1
            ans += 1

    # 마지막 투표를 끝낸 후, 득표 수 빈도를 탐색하며
    # 아직도 빈도가 1보다 큰 항목이 있으면
    # -1 반환
    for i in vote_cnt:
        if i > 1:
            return -1

    # 그렇지 않으면 투표한 횟수 반환
    return ans
