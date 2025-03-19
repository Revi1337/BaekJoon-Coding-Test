import heapq

def solution(s, K):
    answer = 0
    heapq.heapify(s)

    while len(s) > 1:
        food1 = heapq.heappop(s)
        if food1 >= K:
            return answer

        food2 = heapq.heappop(s)
        new_food = food1 + (food2 * 2)
        heapq.heappush(s, new_food)
        answer += 1

    return answer if s[0] >= K else -1