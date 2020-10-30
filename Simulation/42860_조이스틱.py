def solution(name):
    ans = 0
    name = list(name)
    idx = 0

    while True:
        left, right = 1, 1

        if name == ['A'] * len(name):
            break

        if name[idx] != 'A':
            ans += min(ord(name[idx]) - ord('A'), ord('Z') - ord(name[idx]) + 1)
            name[idx] = 'A'

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

'BBBAAAB'
