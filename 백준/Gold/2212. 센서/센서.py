def solution(N, K, guks):
    guks.sort()
    diff = []
    for idx in range(1, N):
        diff.append(guks[idx] - guks[idx - 1])

    diff.sort()
    return sum(diff[:N - K])

N = int(input())
K = int(input())
guks = list(map(int, input().split()))
print(solution(N, K, guks))