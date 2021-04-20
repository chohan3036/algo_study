def solution(routes):
    routes.sort(key=lambda x: x[1])
    cam = -30001

    ans = 0
    for route in routes:
        if cam < route[0]:
            ans += 1
            cam = route[1]

    return ans


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
