def solution(N, number):
    ans = 0
    dp = []

    for i in range(1, 9):
        # 1. number 를 그냥 이어서 만들 수 있는 수
        numbers = set()
        numbers.add(int(str(N) * i))

        for j in range(0, i - 1):
            # 2. j 번째와 전체 - j 번째와의 조합
            # 만들 수 있는 수들을 넣음
            for x in dp[j]:
                for y in dp[-j - 1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            ans = i
            break

        dp.append(numbers)

    return ans if ans != 0 else -1


if __name__ == '__main__':
    print(solution(5, 31168))
