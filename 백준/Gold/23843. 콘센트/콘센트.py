import heapq

def solution(N, M, devices):
    devices.sort(reverse=True)
    pq = [0] * M

    for device in devices:
        time = heapq.heappop(pq)
        heapq.heappush(pq, time + device)

    return max(pq)

N, M = map(int, input().split())
const = list(map(int, input().split()))
print(solution(N, M, const))