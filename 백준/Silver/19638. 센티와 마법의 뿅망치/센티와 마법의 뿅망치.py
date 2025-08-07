import sys, heapq

input = sys.stdin.readline

def solution(N, H, T, arr):
    left = set()
    t = T
    pq = []
    for idx, val in enumerate(arr):
        if val >= H:
            left.add(idx)
        heapq.heappush(pq, [-val, idx])

    while pq and t > 0:
        val, idx = heapq.heappop(pq)
        val = -val
        if val < H:
            heapq.heappush(pq, [val, idx])
            break

        if val == 1:
            heapq.heappush(pq, [1, idx])
        else:
            t -= 1
            val = val // 2
            if val < H:
                left.discard(idx)
            heapq.heappush(pq, [-val, idx])
            if not left:
                break

    pq = [-val for val, _ in pq]
    mx = max(pq)
    return ('YES', T - t) if mx < H else ('NO', mx)

N, H, T = map(int, input().split())
arr = [int(input()) for _ in range(N)]
print(*solution(N, H, T, arr), sep = '\n')