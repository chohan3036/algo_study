import sys
read = lambda: sys.stdin.readline().strip()


def chg_to_map(arr):
    result = []
    for i in range(n):
        tmp = bin(arr[i])[2:]
        if len(tmp) < n:
            tmp = '0' * (n - len(tmp)) + tmp
        result.append(list(map(int, tmp)))
    return result


n = int(read())
arr1 = list(map(int, read().split()))
map1 = chg_to_map(arr1)
arr2 = list(map(int, read().split()))
map2 = chg_to_map(arr2)

real_map = []
for i in range(n):
    tmp_str = ''
    for j in range(n):
        if map1[i][j] == 0 and map2[i][j] == 0:
            tmp_str += ' '
        else:
            tmp_str += '#'
    real_map.append(tmp_str)
print(real_map)

''' rjust : 인수 크기의 빈 문자열을 만들고 문자열을 오른쪽 정렬함
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
'''
