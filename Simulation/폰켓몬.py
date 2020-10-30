def solution(nums):
    half, kinds = len(nums)//2, len(set(nums))
    return min(half, kinds)


print(solution([3, 1, 2, 3]))
