import heapq

'''
아이디어:
나머지 프로세스들의 우선순위를 모두 1씩 올려준다. --> Time Complex 가 O(N) 매우 비효율적
따라서 자기 자신의 우선순위를 1씩 낮추면 된다.
'''
def solution(T, N, processes):
    pq = []
    for pid, time, pri in processes:
        heapq.heappush(pq, [-pri, pid, time])

    for _ in range(T):
        pri, pid, time = heapq.heappop(pq)
        pri = -pri
        print(pid)
        if time - 1 > 0:
            heapq.heappush(pq, [-pri + 1, pid, time - 1])


T, N = map(int, input().split())
processes = [list(map(int, input().split())) for _ in range(N)]
solution(T, N, processes)