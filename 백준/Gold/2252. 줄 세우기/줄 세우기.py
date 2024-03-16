from collections import deque
import sys

input = sys.stdin.readline

def solution(n, m, edges):
    counter = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edges:
        counter[v2] += 1
        graph[v1].append(v2)

    answer = []
    queue = deque()
    for student, count in enumerate(counter[1:], start=1):
        if not count:
            answer.append(student)
            queue.append(student)

    while queue:
        student = queue.popleft()
        for next_student in graph[student]:
            counter[next_student] -= 1
            if not counter[next_student]:
                answer.append(next_student)
                queue.append(next_student)

    return " ".join(map(str, answer))

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, edges))