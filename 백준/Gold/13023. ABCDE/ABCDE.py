""" BackTracking """
def solution(n, m, friends):
    friend_cnt = n
    relationships = [[] for _ in range(friend_cnt)]
    for friend1, friend2, in friends:
        relationships[friend1].append(friend2)
        relationships[friend2].append(friend1)

    answer = 0
    def dfs(friend, depth):
        nonlocal answer
        if depth == 4:
            answer = 1
            return
        for next_friend in relationships[friend]:
            if not check[next_friend]:
                check[next_friend] = 1
                dfs(next_friend, depth + 1)
                check[next_friend] = 0
        return answer

    for friend in range(friend_cnt):
        check = [0] * friend_cnt
        if not check[friend]:
            check[friend] = 1
            answer = dfs(friend, 0)
            if answer: break

    return answer

n, m = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, friends))

