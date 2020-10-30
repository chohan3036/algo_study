from collections import deque


def solution(m, k):
    m, k = deque(m), deque(k)
    ans = ''
    ans.