def solution(inputString):
    open = {'(': 0, '{': 0, '[': 0, '<': 0}
    close = {')': '(', '}': '{', ']': '[', '>': '<'}
    ans = 0
    for char in inputString:
        if char in open:
            open[char] += 1
        elif char in close:
            if open[close[char]] == 0:
                return -1
            else:
                open[close[char]] -= 1
                if open[close[char]] == 0:
                    ans += 1

    for key in open:
        if open[key] > 0:
            return -1

    return ans


print(solution('>>><<<'))
