import heapq as hq


def solution(scoville, k):
    ans = 0
    hq.heapify(scoville)

    while scoville:
        min1 = hq.heappop(scoville)

        if min1 >= k:
            break

        if not scoville:
            ans = -1
            break

        min2 = hq.heappop(scoville)
        score = min1 + min2 * 2
        hq.heappush(scoville, score)

        ans += 1

    return ans


print(solution([7, 5, 1, 10, 3, 2], 50))
