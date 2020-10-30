def solution(n):
    notation, ans = 2, 1
    for k in range(2, 10):
        cnt = 1
        num_list = [1]
        while True:
            # k * 현재 자릿수
            cur_num = k ** cnt
            num_list.append(cur_num)
            cnt += 1
            if cur_num >= 1000000:
                break

        num_list.sort(reverse=True)
        num = n
        notated = 1
        while num > 0:
            for i in num_list:
                if i <= num:
                    notated *= num // i
                    num %= i

        if ans <= notated:
            notation = k
            ans = notated

    return [notation, ans]


print(solution(10))
