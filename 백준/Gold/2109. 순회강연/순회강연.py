import heapq

def solution(N, arr):
    arr.sort(key=lambda x: x[1], reverse=True)
    max_day = max(d for _, d in arr) if arr else 0

    pq = []
    answer = 0
    idx = 0

    for day in range(max_day, 0, -1):
        while idx < N and arr[idx][1] >= day:
            heapq.heappush(pq, -arr[idx][0])
            idx += 1
        if pq:
            answer += -heapq.heappop(pq)
    return answer

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, arr))