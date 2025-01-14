import heapq

def solution(N, classes):
    classes.sort(key = lambda x: (x[1], x[2]))

    pq = [classes[0][2]]
    for idx in range(1, N):
        if pq[0] > classes[idx][1]:
            heapq.heappush(pq, classes[idx][2])
        else:
            heapq.heappop(pq)
            heapq.heappush(pq, classes[idx][2])

    return len(pq)

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, classes))