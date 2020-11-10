def solution(s):
    cnt = zero = 0
    while True:
        if s == '1':
            return [cnt, zero]

        cur_zero = s.count('1')
        s = str(bin(cur_zero))[2:]
        cnt += 1


print(solution("1111111"))
