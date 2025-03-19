from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = 1e9
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        check = [0] * (n + 1)
        diff = [0, 0]
        offset = 0
        for node in range(1, n + 1):
            if not check[node]:
                check[node] = 1
                queue = deque([node])
                cnt = 1
                while queue:
                    v = queue.popleft()
                    cnt += 1
                    for nv in graph[v]:
                        if not check[nv]:
                            check[nv] = 1
                            queue.append(nv)
                diff[offset] = cnt
                offset += 1

        answer = min(answer, abs(diff[0] - diff[1]))
        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer