import sys
import heapq

input = sys.stdin.readline

def solution(n, m, citys, prolog, epilog):
    graph = [[] for _ in range(n + 1)]
    for city1, city2, cost in citys:
        graph[city1].append([city2, cost])

    costs = [float('inf') for _ in range(n + 1)]
    costs[prolog] = 0
    priority_queue = []

    heapq.heappush(priority_queue, [costs[prolog], prolog])
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        if costs[node] < cost:
            continue
        for next_city, next_cost in graph[node]:
            predicate_cost = cost + next_cost
            if predicate_cost < costs[next_city]:
                costs[next_city] = predicate_cost
                heapq.heappush(priority_queue, [predicate_cost, next_city])

    print(costs[epilog])

n = int(input())
m = int(input())
citys = [list(map(int, input().split())) for _ in range(m)]
prolog, epilog = map(int, input().split())
solution(n, m, citys, prolog, epilog)
