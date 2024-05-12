def solution(T, N, M, A, B):
    max_length, min_length = max([N, M]), min([N, M])
    mutable = [0] * max_length
    immutable = None
    if min_length == N:
        for idx in range(min_length):
            mutable[idx] = A[idx]
            immutable = B[::]
    else:
        for idx in range(min_length):
            mutable[idx] = B[idx]
            immutable = A[::]

    answer = sum([mutable[idx] * immutable[idx] for idx in range(min_length)])
    right = min_length - 1
    while right < max_length:
        answer = max(answer, sum([mutable[idx] * immutable[idx] for idx in range(max_length)]))
        mutable.insert(0, mutable.pop())
        right += 1

    return f'#{T} {answer}'

T = int(input())
for idx in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solution(idx + 1, N, M, A, B))