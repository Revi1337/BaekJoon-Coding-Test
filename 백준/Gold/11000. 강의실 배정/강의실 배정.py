import heapq

'''
먼저 시작한 것 중 먼저 끝난 것.
'''
def solution(N, classes):
    classes.sort()
    pq = [classes[0][1]]

    for st, end in classes[1:]:
        if pq[0] > st:
            heapq.heappush(pq, end)
        else:
            heapq.heappop(pq)
            heapq.heappush(pq, end)

    return len(pq)

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, classes))
