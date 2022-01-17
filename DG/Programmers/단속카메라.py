def solution(routes):
    answer = 0

    sortedRoutes = sorted(routes, key=lambda x: x[1])

    lastCamera = -30001

    for route in sortedRoutes:
        if route[0] > lastCamera:
            answer += 1
            lastCamera = route[1]

    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

print(solution(routes))
