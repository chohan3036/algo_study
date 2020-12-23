def solution(msg):
    # key: 알파벳 value: 숫자
    dic = {chr(i + 64): i for i in range(1, 27)}
    last = 26

    ans = []
    idx = -1
    while idx < len(msg) - 1:
        idx += 1
        word = msg[idx]

        # word 를 한 글자씩 늘려가며 사전에 존재하는지 검색
        while idx + 1 < len(msg):
            word += msg[idx + 1]

            # 사전 안에 없으면 사전에 해당 글자 추가해주고
            # word는 추가했던 한 글자 도로 빼기
            if word not in dic:
                last += 1
                dic[word] = last
                word = word[:-1]
                break

            # 사전 안에 있으면
            # 다음 인덱스를 늘린 글자 수만큼 넘김
            idx += 1

        # 사전에 있고, 최대한 늘린 글자의 색인 번호 저장
        ans.append(dic[word])

    return ans
