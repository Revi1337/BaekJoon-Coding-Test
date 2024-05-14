def solution(seq, N):
    maxN = max(N)
    integers = [0] * (maxN + 1)
    for integer in N:
        integers[integer] += 1
    prev = answer = -1e9
    for integer in range(maxN + 1):
        if integers[integer] >= prev:
            prev = integers[integer]
            answer = integer
    return f'#{seq} {answer}'

T = int(input())
for idx in range(T):
    seq = int(input())
    N = list(map(int, input().split()))
    print(solution(seq, N))
    