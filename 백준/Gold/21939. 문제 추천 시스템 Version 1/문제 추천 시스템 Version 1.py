import sys
import heapq

input = sys.stdin.readline

def solution(N, P, M, OP):
    P1, P2, prob = [], [], dict()

    for num, lv in P:
        prob[num] = lv
        heapq.heappush(P1, [-lv, -num])
        heapq.heappush(P2, [lv, num])

    for op, *codes in OP:
        if op == 'recommend':
            x = int(codes[0])
            if x == 1:
                while True:
                    lv, num = heapq.heappop(P1)
                    lv, num = -lv, -num
                    if num in prob and prob[num] == lv:
                        print(num)
                        heapq.heappush(P1, [-lv, -num])
                        break
            else:
                while True:
                    lv, num = heapq.heappop(P2)
                    if num in prob and prob[num] == lv:
                        print(num)
                        heapq.heappush(P2, [lv, num])
                        break
        elif op == 'add':
            num, lv = map(int, codes)
            prob[num] = lv
            heapq.heappush(P1, [-lv, -num])
            heapq.heappush(P2, [lv, num])
        elif op == 'solved':
            num = int(codes[0])
            if num in prob:
                prob.pop(num)

N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
OP = [input().rstrip().split() for _ in range(M)]
solution(N, P, M, OP)