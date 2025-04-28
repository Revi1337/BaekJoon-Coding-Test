import heapq

def solution(K, files):
    heapq.heapify(files)
    sm = 0
    while K > 2:
        f1 = heapq.heappop(files)
        f2 = heapq.heappop(files)
        K -= 2
        sm += f1 + f2
        heapq.heappush(files, f1 + f2)
        K += 1

    return sm + sum(files)

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    print(solution(K, files))
