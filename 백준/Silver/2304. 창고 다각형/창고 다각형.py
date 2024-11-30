def solution(N, builds):
    size = max(builds, key = lambda x: x[0])[0] + 1
    buildings = [0] * size
    max_height = 0
    for idx in range(N):
        num, height = builds[idx]
        buildings[num] = height
        max_height = max(max_height, buildings[num])

    answer = 0
    for curr_height in range(1, max_height + 1):
        s_idx = e_idx = 0
        for idx in range(1, size):
            if buildings[idx] >= curr_height:
                if s_idx == 0:
                    s_idx = idx
                e_idx = idx
        if s_idx:
            answer += (e_idx - s_idx + 1)

    return answer

N = int(input())
builds = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, builds))
