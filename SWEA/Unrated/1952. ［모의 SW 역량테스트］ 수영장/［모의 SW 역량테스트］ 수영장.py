def solution(costs, months):
    answer = [1e9] * 12
    answer.extend([0] * 4)
    for month in range(11, -1, -1):
        for idx in range(4):
            if not months[month]:
                answer[month] = answer[month + 1]
                continue

            tmp = 1e9
            for idx in range(3):
                if idx == 0:
                    tmp = min(tmp, costs[idx] * months[month] + answer[month + 1])
                elif idx == 1:
                    tmp = min(tmp, costs[idx] + answer[month + 1])
                elif idx == 2:
                    for m in range(month + 1, month + 4):
                        tmp = min(tmp, costs[idx] + answer[m])
            answer[month] = tmp

    return min(answer[0], costs[3])

T = int(input())
for t in range(1, T + 1):
    costs = list(map(int, input().split()))
    months = list(map(int, input().split()))
    print(f'#{t} {solution(costs, months)}')
