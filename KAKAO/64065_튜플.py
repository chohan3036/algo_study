import re


def solution(s):
    ans = []
    s = list(map(str, s.split('},{')))
    s.sort(key=len)
    for x in s:
        numbers = re.findall("\d+", x)
        for n in numbers:
            if int(n) not in ans:
                ans.append(int(n))
    return ans


if __name__ == '__main__':
    print(solution("{{2}}"))