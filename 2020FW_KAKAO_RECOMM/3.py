#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'editDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING source
#  2. STRING target
#
def shift(n, word, target):
    new_word = ''
    cnt = 0
    for i in range(n):
        if 97 <= ord(word[i]) < 97 + 25:
            new_char = chr(ord(word[i]) + 1)
        else:
            new_char = 'a'
        new_word += new_char

        if new_char == target[i]:
            cnt += 1

    return new_word, cnt


def editDistance(source, target):
    n = len(source)
    # shift 먼저 수행하여 최대한 비슷한 문자열로 만들기
    new_source = ''
    max_similarity = 0
    shifted = '' + source
    for _ in range(25):
        shifted, similarity = shift(n, shifted, target)
        if max_similarity < similarity:
            new_source = shifted
            max_similarity = similarity

    if new_source == target:
        return 0

    # levenshtein 알고리즘 사용
    # 문자열에 각각 삽입, 삭제, 교체 세 연산에 대한 비용을 dp로 갱신해 나감
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0 if new_source[0] != target[0] else 1
    for i in range(n):
        for j in range(n):
            # 행이나 열이 0일 땐 글자 삽입만 수행할 수 있으므로
            if i == 0:
                dp[i][j] = dp[i][j - 1] + 1
                continue
            if j == 0:
                dp[i][j] = dp[i - 1][j] + 1
                continue

            insert = dp[i - 1][j] + 1
            delete = dp[i][j - 1]
            substit = dp[i - 1][j - 1] + (new_source[j] != target[j])  # 여기가 잘 안 됨
            dp[i][j] = min(insert, delete, substit)

    return dp


print(editDistance('abd', 'gzu'))
