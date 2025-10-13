def solution(N, A1, A2):
    ind1 = {}
    for idx in range(N):
        ind1[A1[idx]] = set(A1[idx:])

    ind2 = {A2[0]: set()}
    for idx in range(1, N):
        ind2[A2[idx]] = {*ind2[A2[idx - 1]], A2[idx - 1]}

    ans = set()
    for car in A2:
        ans = ans | (ind2[car] & ind1[car])

    return len(ans)

N = int(input())
A1 = [input().rstrip() for _ in range(N)]
A2 = [input().rstrip() for _ in range(N)]
print(solution(N, A1, A2))
