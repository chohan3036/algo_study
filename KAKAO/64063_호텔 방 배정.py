# 선형으로 하면 O(N^2)
# 그럼.. 이분탐색이나 트리
# 딕셔너리 많이 써야 해요


def solution(k, room_number):
    ans, rooms = [], {}

    # 손님 목록을 순회하며 확인
    for number in room_number:
        # 방 확인 - 다른 값이 있으면 가져오고, 아니면 0을 줌
        room = rooms.get(number, 0)

        # 방이 이미 배정 됐다면
        if room:
            tmp = [number]
            # 빈 방 찾기
            while True:
                # 다음으로 배정해 줄 방 번호를 저장
                idx = room
                # 다음으로 지목된 방이 비었는지 확인
                room = rooms.get(room, 0)
                # 만약 이 방이 비어있지 않으면
                if not room:
                    ans.append(idx)
                    rooms[idx] = idx + 1
                    for t in tmp:
                        rooms[t] = idx + 1
                    break
                tmp.append(room)

        # 원하는 방이 비어있으면 바로 배정
        # 배정한 뒤 하나 큰 인덱스 저장
        else:
            ans.append(number)
            rooms[number] = number + 1
    return ans


print(10, [1, 3, 4, 1, 3, 1])
