from collections import deque

def solution(N, S, datas):
    max_num = max(datas)
    graph = [[] for _ in range(max_num + 1)]
    for idx in range(0, N, 2):
        fro, to = datas[idx], datas[idx + 1]
        graph[fro].append(to)

    check = [0] * (max_num + 1)
    check[S] = 1
    answer = S
    queue = deque([S])

    while queue:
        node = queue.popleft()
        if check[node] > check[answer] or (check[answer] == check[node] and answer < node):
            answer = node
        for next_node in graph[node]:
            if not check[next_node]:
                check[next_node] = check[node] + 1
                queue.append(next_node)

    return answer

T = 10
for seq in range(T):
    N, S = map(int, input().split())
    datas = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, S, datas)}')
