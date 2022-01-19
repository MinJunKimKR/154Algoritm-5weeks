def solution(N, stages):

    data = {}
    total = len(stages)
    for stage in range(1, N+1):
        if total != 0:
            count = stages.count(stage)
            data[stage] = count / total
            total -= count
        else:
            data[stage] = 0

    answer = sorted(data, key=lambda x: data[x], reverse=True)

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))