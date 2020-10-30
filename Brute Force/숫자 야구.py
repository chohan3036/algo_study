from itertools import permutations

baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]

num = [str(i) for i in range(1, 10)]
can = list(map(''.join, permutations(num, 3)))

for guess, strike, ball in baseball:
    guess = str(guess)
    tmp = []
    for c in can:
        cur_strike, cur_ball = 0, 0
        for i in range(3):
            # 위치와 숫자가 맞을 때
            if c[i] == guess[i]:
                cur_strike += 1
            # 숫자만 맞을 때
            if c[i] in guess:
                cur_ball += 1

        if strike == cur_strike and ball == cur_ball - cur_strike:
            tmp.append(c)
    can = tmp

print(len(can))
