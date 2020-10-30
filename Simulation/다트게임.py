dartResult = '1D2S#10S'
num = list(map(str, [i for i in range(11)]))

score = []
idx = 0
for i in range(len(dartResult)):
    if dartResult[i] in num and i != 0:
        if dartResult[i - 1] == '1' and dartResult[i] == '0':
            continue
        score.append(dartResult[idx: i])
        idx = i

    if i == len(dartResult) - 1:
        score.append(dartResult[idx:])

print(score)

operand = [[] for _ in range(3)]
for i in range(3):
    # 기본 점수 책정
    if score[i][0: 2] == '10':
        cur_score = 10
    else:
        cur_score = int(score[i][0])

    if 'S' in score[i]:
        operand[i].append(cur_score)
    elif 'D' in score[i]:
        operand[i].append(pow(cur_score, 2))
    elif 'T' in score[i]:
        operand[i].append(pow(cur_score, 3))

    # 옵션 책정
    if '*' in score[i]:
        operand[i].append(2)
        if i != 0:
            operand[i - 1].append(2)

    if '#' in score[i]:
        operand[i].append(-1)

print(operand)


def multiply(arr):
    return eval('*'.join([str(n) for n in arr]))


answer = 0
for i in range(3):
    answer += multiply(operand[i])


'''
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

'''