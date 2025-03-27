def solution(N, M, A, B):
    A, B = set(A), set(B)
    C = A - B

    length = len(C)
    print(len(C))
    if length:
        print(*sorted(C), sep = ' ')


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
solution(N, M, A, B)