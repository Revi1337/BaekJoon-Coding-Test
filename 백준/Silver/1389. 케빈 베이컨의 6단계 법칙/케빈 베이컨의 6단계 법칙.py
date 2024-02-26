from collections import deque

def solution(n, m, edges):
    vertext_cnt = n
    relationships = [[] for _ in range(vertext_cnt + 1)]
    for friend1, friend2 in edges:
        relationships[friend1].append(friend2)
        relationships[friend2].append(friend1)

    answer = [0] * (vertext_cnt + 1)

    for entrypoint in range(1, vertext_cnt + 1):
        distance = [0] * (vertext_cnt + 1)
        check = [0] * (vertext_cnt + 1)
        queue = deque([entrypoint])
        distance[entrypoint] = 0
        check[entrypoint] = 1
        while queue:
            curr_friend = queue.popleft()
            for next_friend in relationships[curr_friend]:
                if not check[next_friend] and distance[next_friend] == 0:
                    distance[next_friend] = distance[curr_friend] + 1
                    check[next_friend] = 1
                    queue.append(next_friend)
        answer[entrypoint] = sum(distance)

    min_friend = min(answer[1:])
    for friend in range(1, vertext_cnt + 1):
        if answer[friend] == min_friend:
            return friend

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, edges))
