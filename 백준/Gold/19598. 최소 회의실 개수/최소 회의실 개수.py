import heapq

def solution(N, classes):
    classes.sort()
    pq = [classes[0][1]]
    for _, (start, end) in enumerate(classes[1:], start = 1):
        if pq[0] > start:
            heapq.heappush(pq, end)
        else:
            heapq.heappop(pq)
            heapq.heappush(pq, end)

    return len(pq)

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, classes))
