import heapq

def solution(N, road, K):
    houst_cnt = N
    houses = [[] for _ in range(houst_cnt + 1)]
    for house1, house2, time in road:
        houses[house1].append([house2, time])
        houses[house2].append([house1, time])

    times = [float('inf') for _ in range(houst_cnt + 1)]
    paths = [float('inf') for _ in range(houst_cnt + 1)]

    times[1] = 0
    paths[1] = [1]

    queue = []
    heapq.heappush(queue, [times[1], 1])
    while queue:
        curr_cost, curr_house = heapq.heappop(queue)
        for next_house, next_cost in houses[curr_house]:
            predicate_time = curr_cost + next_cost
            if predicate_time < times[next_house]:
                times[next_house] = predicate_time
                paths[next_house] = paths[curr_house] + [next_house]
                heapq.heappush(queue, [predicate_time, next_house])

    return sum([1 for time in times if time <= K])