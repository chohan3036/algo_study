def solution(name):
    # 우선 cnt 리스트에 위아래 조작 횟수만 넣어놓음
    ans = 0
    name = list(name)
    idx = 0
    # 왼오 조작?
    while True:
        left, right = 1, 1
        if name[idx] != 'A':
            ans += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)
            name[idx] = 'A'
        if name == ['A'] * len(name):
            break
        for i in range(1, len(name)):
            if name[idx + i] == 'A':
                right += 1
            else:
                break

        for i in range(1, len(name)):
            if name[idx - i] == 'A':
                left += 1
            else:
                break

        if left >= right:
            ans += right
            idx += right
        else:
            ans += left
            idx -= left

    return ans


if __name__ == '__main__':
    print(solution('BBBAAAB'))
