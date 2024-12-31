from collections import deque

def solution(N, K, A):
    start, end = 0, N - 1
    length = 2 * N
    z_cnt = answer = 0

    queue, robots = deque([*A]), deque([0] * length)
    while z_cnt < K:
        queue.rotate(1)
        robots.rotate(1)
        robots[end] = 0

        for idx in range(N - 2, -1, -1):
            if robots[idx] and not robots[idx + 1] and queue[idx + 1] > 0:
                robots[idx], robots[idx + 1] = 0, 1
                queue[idx + 1] -= 1
                if queue[idx + 1] == 0:
                    z_cnt += 1
        robots[end] = 0

        if not robots[start] and queue[start] > 0:
            robots[start] = 1
            queue[start] -= 1
            if queue[start] == 0:
                z_cnt += 1

        answer += 1

    return answer


N, K = map(int, input().split())
A = list(map(int, input().split()))
print(solution(N, K, A))
