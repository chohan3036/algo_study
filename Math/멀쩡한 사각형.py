from math import gcd


def solution(w,h):
    great = gcd(w, h)
    gw, gh = w // great, h // great
    answer = w * h - (gw + gh - 1) * great
    return answer
