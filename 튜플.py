import re
from collections import Counter


def solution(s):
    num = Counter(re.findall("\d+", s))
    ans = sorted(num.items(), key=lambda x: -x[1])
    return [int(x[0]) for x in ans]
