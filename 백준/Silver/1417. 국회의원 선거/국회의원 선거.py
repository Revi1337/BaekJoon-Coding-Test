import sys
import heapq

input = sys.stdin.readline

def solution(n, votes):
    if n == 1:
        return 0

    queue = []
    for idx in range(n):
        if idx != 0:
            heapq.heappush(queue, (-votes[idx], votes[idx]))

    dasom = votes[0]
    answer = 0
    while True:
        max_vote = heapq.heappop(queue)[1]
        if max_vote < dasom:
            return answer
        answer += 1
        dasom += 1
        heapq.heappush(queue, (-(max_vote - 1), max_vote - 1))

n = int(input().rstrip())
votes = [int(input().rstrip()) for _ in range(n)]
print(solution(n, votes))
