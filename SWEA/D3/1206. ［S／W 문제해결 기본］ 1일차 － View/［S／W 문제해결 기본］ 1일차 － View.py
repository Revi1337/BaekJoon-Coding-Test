def solution(idx, N, building):
    answer = 0
    for i in range(2, N - 2):
        if max(building[i - 2: i + 3]) == building[i]:
            max_building = max(max(building[i - 2: i]), max(building[i + 1: i + 3]))
            answer += (building[i] - max_building)
    return f'#{idx} {answer}'

T = 10
for idx in range(T):
    N = int(input())
    building = list(map(int, input().split()))
    print(solution(idx + 1, N, building))
