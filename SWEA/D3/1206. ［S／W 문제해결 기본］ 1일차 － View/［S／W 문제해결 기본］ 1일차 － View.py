def solution(index, N, buildings):
    answer = 0
    for idx in range(2, N - 2):
        if max(buildings[idx - 2 : idx + 3]) == buildings[idx]:
            second_max_building = max(max(buildings[idx - 2 : idx]), max(buildings[idx + 1 : idx + 3]))
            answer += buildings[idx] - second_max_building

    return f'#{index} {answer}'

T = 10
for idx in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))
    print(solution(idx + 1, N, buildings))