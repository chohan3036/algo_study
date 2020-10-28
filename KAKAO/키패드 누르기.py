from collections import defaultdict


def solution(numbers, hand):
    key_dic = defaultdict()
    idx = 1
    for i in range(3):
        for j in range(3):
            key_dic[idx] = (i, j)
            idx += 1
    key_dic['*'], key_dic[0], key_dic['#'] = (3, 0), (3, 1), (3, 2)

    answer = ''
    lf, rf = key_dic['*'], key_dic['#']
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            lf = key_dic[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            rf = key_dic[n]
        else:
            lf_dist = abs(lf[0] - key_dic[n][0]) + abs(lf[1] - key_dic[n][1])
            rf_dist = abs(rf[0] - key_dic[n][0]) + abs(rf[1] - key_dic[n][1])
            if lf_dist == rf_dist:
                if hand == 'left':
                    lf = key_dic[n]
                    answer += 'L'
                else:
                    rf = key_dic[n]
                    answer += 'R'
            elif lf_dist < rf_dist:
                lf = key_dic[n]
                answer += 'L'
            else:
                rf = key_dic[n]
                answer += 'R'

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
