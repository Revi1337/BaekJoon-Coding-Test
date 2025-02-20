def solution(N, hunies):
    psum = [0] * N
    psum[0] = hunies[0]
    for idx in range(1, N):
        psum[idx] = psum[idx - 1] + hunies[idx]

    answer = 0
    for idx in range(1, N - 1):
        sm1 = (psum[idx] - hunies[0]) + (psum[-2] - psum[idx - 1]) # (왼쪽 벌 0 고정. 오른쪽 벌 N - 1 고정. 벌통이 1 ~ N - 2 범위를 순회)
        sm2 = (psum[-1] - hunies[0] - hunies[idx]) + (psum[-1] - psum[idx]) # (왼쪽 벌 0 고정. 벌통 N - 1 고정. 오른쪽 벌이 1 ~ N - 2 범위를 순회)
        sm3 = (psum[-1] - hunies[-1] - hunies[idx]) + (psum[idx - 1]) # (벌통 0 고정, 오른쪽 벌 N - 1 고정. 왼쪽 벌이 1 ~ N - 2 범위를 순회)
        answer = max(answer, sm1, sm2, sm3)

    return answer

N = int(input())
hunies = list(map(int, input().rstrip().split()))
print(solution(N, hunies))