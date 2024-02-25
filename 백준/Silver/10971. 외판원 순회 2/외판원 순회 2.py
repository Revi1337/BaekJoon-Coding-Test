"""
V1. check 배열을 별도로 생성하는 방법
- 첫 정점이 시작될때(34Line 의 for 문) 새롭게 check 를 선언해주어야 한다. 
  (첫 정점이 끝났을때 check 를 다시 초기화 하지 않으면 두번째 정점이 시작될때 기존 check 를 쓰게되어 이상해진다.)
"""
def solution(n, graph):
    vertext_cnt = n
    answer = float('inf')

    def dfs(entrypoint, curr_vertext, cost):
        nonlocal answer
        if check == [1] * vertext_cnt:
            return_cost = graph[curr_vertext][entrypoint]
            if return_cost:
                answer = min(answer, cost + return_cost)
            return

        for next_vertext in range(vertext_cnt):
            next_cost = graph[curr_vertext][next_vertext]
            if (next_cost) and (not check[next_vertext]) and (cost < answer):
                check[next_vertext] = 1
                dfs(entrypoint, next_vertext, cost + next_cost)
                check[next_vertext] = 0

    for vertext in range(vertext_cnt):
        check = [0] * vertext_cnt
        check[vertext] = 1
        dfs(vertext, vertext, 0)

    return answer

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, edges))


"""
V2. check 배열을 dfs 의 매개변수로 전달해주는 방법
- 첫 정점이 시작될때(70Line 의 for 문) 새롭게 check 를 선언해주지 않아도 된다.
  (왜냐하면 정점이 시작될떄 새롭게 [정점] 으로 check 배열을 생성하고 있기 때문이다.)
"""
def solution(n, graph):
    vertext_cnt = n
    answer = float('inf')

    def dfs(entrypoint, curr_vertext, cost, check):
        nonlocal answer
        if len(check) == vertext_cnt:
            return_cost = graph[curr_vertext][entrypoint]
            if return_cost:
                answer = min(answer, cost + return_cost)
            return

        for next_vertext in range(vertext_cnt):
            next_cost = graph[curr_vertext][next_vertext]
            if (next_cost) and (next_vertext not in check) and (cost < answer):
                check.append(next_vertext)
                dfs(entrypoint, next_vertext, cost + next_cost, check)
                check.pop()

    for vertext in range(vertext_cnt):
        dfs(vertext, vertext, 0, [vertext])

    return answer

n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, edges))
