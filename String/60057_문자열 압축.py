def solution(string):
    min_len = len(string)

    for i in range(1, len(string) // 2 + 1):
        idx1, idx2 = 0, i   # 부분 비교할 인덱스
        stack = ''          # 검사한 문자열들을 저장할 stack
        cnt = 0             # 몇 번 압축하는지

        while True:
            # 앞, 뒤 부분 문자열
            first = string[idx1: idx1 + i]
            second = string[idx2: idx2 + i]

            # 부분 문자열이 같을 경우, 압축 횟수 + 1 해줌
            if first == second:
                cnt += 1
            # 부분 문자열이 다를 경우
            else:
                # 이전에 압축을 했으면
                # 압축이 가능한 횟수와 해당 부분 문자열을 이어서 stack 에 저장
                # 압축 횟수 초기화
                if cnt > 0:
                    stack += str(cnt + 1) + first
                    cnt = 0
                # 압축한 적이 없으면 해당 문자열을 그냥 stack 에 저장
                else:
                    stack += first

            # 부분 문자열을 만들 수 있을만큼의 길이가 남지 않았으면
            # 남은 거 그냥 다 stack 에 붙이고 끝내기
                if idx2 > len(string) - i:
                    stack += string[idx2:]
                    break

            # step 더해주기
            idx1, idx2 = idx2, idx2 + i

        # stack 완성되면 최소 길이 갱신하기
        min_len = min(min_len, len(stack))

    return min_len


print(solution("ababcdcdababcdcd"))
