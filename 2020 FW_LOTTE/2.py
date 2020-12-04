def solution(n, k):
    # k번째까지 관람객의 위치를 순서대로 갱신할 리스트
    # 1번째 관람객은 항상 [0, 0]
    seats = [[0, 0]]

    # 관람객이 추가됨에 따라 달라지는 거리를 갱신할 리스트
    # 대략적인 최대 거리를 저장해 놓음
    dists = [[2 * n for _ in range(n)] for _ in range(n)]

    # k번째 관람객까지 배치하며 거리를 갱신
    for num in range(1, k + 1):
        # 가장 최근에 배치된 관람객의 위치
        x, y = seats[num - 1]

        next_seat, max_dist = [0, 0], 0
        for i in range(n):
            for j in range(n):
                # 관람객이 추가됨에 따라 최대 거리가 줄어듦
                # min을 사용해 갱신된 거리를 취하도록 함
                dists[i][j] = min(dists[i][j], abs(x - i) + abs(y - j))

                # 이 중 가장 먼 거리를 갱신하며
                # 다음 관람객의 좌석을 정해줌
                if max_dist < dists[i][j]:
                    max_dist = dists[i][j]
                    next_seat[0], next_seat[1] = i, j

                # 거리가 같을 경우에도 열이나 행의 번호가 더 적다면
                # 해당 좌석으로 갱신
                elif max_dist == dists[i][j]:
                    # 열 -> 행 순으로 비교
                    if next_seat[1] > j or (next_seat[1] == j and next_seat[0] > i):
                        next_seat[0], next_seat[1] = i, j

        seats.append(next_seat)

    # 0부터 시작하는 인덱스를 사용했으므로
    # 1씩 더해줌
    return [seats[k - 1][0] + 1, seats[k - 1][1] + 1]