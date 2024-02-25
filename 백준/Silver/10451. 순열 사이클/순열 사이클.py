import sys

sys.setrecursionlimit(10 ** 5)

def solution(n, cycle):
    vertext_cnt = n
    graph = [[] for _ in range(vertext_cnt + 1)]
    for vertext, next_vertext in enumerate(cycle, start=1):
        graph[vertext].append(next_vertext)

    def dfs(vertext):
        check[vertext] = 1
        for next_vertext in graph[vertext]:
            if not check[next_vertext]:
                dfs(next_vertext)

    answer = 0
    check = [0] * (vertext_cnt + 1)
    for vertext in range(1, vertext_cnt + 1):
        if not check[vertext]:
            answer += 1
            dfs(vertext)

    return answer

t = int(input())
for _ in range(t):
    n = int(input())
    cycle = list(map(int, input().split()))
    print(solution(n, cycle))

"""
IDE 를 지원하는 환경도 있나..
"""