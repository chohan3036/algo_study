'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
import re
from collections import deque
from copy import deepcopy


rule = ['a', 'b', 'c', 'd', 'e',
        'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y',
        'z', '-', '_', '.']


def solution(new_id):
    # 1단계
    ans = new_id.lower()
    print(ans)

    # 2단계
    ans = deque(ans)
    for i in range(len(ans)):
        cur_char = ans.popleft()
        if cur_char in rule or cur_char.isdigit():
            ans.append(cur_char)
    ans = ''.join(x for x in ans)
    print(ans)

    # 3단계
    while True:
        tmp = ans.replace('..', '.')
        if tmp != ans:
            ans = deepcopy(tmp)
        else:
            break
    print(ans)

    # 4단계
    ans = ans.strip('.')
    print(ans)

    # 5단계
    if not ans:
        ans = 'a'
    print(ans)

    # 6단계
    if len(ans) >= 16:
        ans = ans[: 15]
    ans = ans.strip('.')
    print(ans)

    # 7단계
    if len(ans) <= 2:
        while len(ans) < 3:
            ans += ans[-1]
    print(ans)

    return ans


print(solution("123_.def"))
