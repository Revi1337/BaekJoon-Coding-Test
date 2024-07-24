import sys
from collections import deque

input = sys.stdin.readline

def solution(N, words):
    answer = 0
    cache = set()
    for word in words:
        if word not in cache:
            answer += 1
            cache.add(word)

        queue = deque(word)
        for _ in range(len(word)):
            queue.rotate(-1)
            string = "".join(queue)
            cache.add(string)

    return answer


N = int(input())
words = [input().strip() for _ in range(N)]
print(solution(N, words))
