import sys
import heapq

input = sys.stdin.readline

def solution(n, m, x, edges):
    graph = [[] for _ in range(n + 1)]
    for v1, v2, cost in edges:
        graph[v1].append([v2, cost])

    def dijkstra(house):
        priority_queue = []
        times[house] = 0
        heapq.heappush(priority_queue, [times[house], house])
        while priority_queue:
            time, home = heapq.heappop(priority_queue)
            if time > times[home]:
                continue
            for next_home, next_cost in graph[home]:
                predicate_time = time + next_cost
                if predicate_time < times[next_home]:
                    times[next_home] = predicate_time
                    heapq.heappush(priority_queue, [predicate_time, next_home])
        return times

    answer = [[]]
    for house in range(1, n + 1):
        times = [float('inf')] * (n + 1)
        answer.append(dijkstra(house))

    time_list = []
    for i in range(1, n + 1):
        time_list.append(answer[i][x] + answer[x][i])

    return max(time_list)

n, m, x = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, x, edges))