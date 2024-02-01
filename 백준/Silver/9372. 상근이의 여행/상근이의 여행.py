from collections import deque

def solution(n, positions):
    graph = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)
    for v1, v2 in positions:
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = -1
    check = [0] * (n + 1)
    queue = deque()
    queue.append(graph[1])
    while queue:
        vertext_cnt = len(queue)
        for _ in range(vertext_cnt):
            vertext = queue.popleft()
            for next_vertext in vertext:
                if check[next_vertext] == 0:
                    queue.append(graph[next_vertext])
                    check[next_vertext] = 1
                    answer += 1
    return answer

loop = int(input())
for _ in range(loop):
    n, m = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, positions))