n = int(input())
sList = []
result = []
for i in range(n):
    sList = list(map(str, input()))
    result.append([])

    if (len(sList) < 2) | (len(sList) > 50): # 배열 크기
        continue
    if len(sList) % 2 == 1: # 괄호가 홀수개면 No 때리고 끝
        result[i] = 'NO'
        continue
    if sList.count('(') != sList.count(')'):
        result[i] = 'NO'
        continue
    if sList[0] == ')':
        result[i] = 'NO'
        continue

    temp = []
    for j in range(len(sList)):
        temp.append(sList[j])
        if (temp[len(temp) - 2] == '(') & (temp[len(temp) - 1] == ')'):
            del temp[len(temp) - 2]
            del temp[len(temp) - 1]

    if len(temp) > 0:
        result[i] = 'NO'
    else:
        result[i] = 'YES'

for i in range(n):
    print(result[i])