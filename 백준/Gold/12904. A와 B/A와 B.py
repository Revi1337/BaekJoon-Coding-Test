def solution(S, T):
    length = len(S)
    while len(T) > length:
        if T[-1] == 'B':
            T = T[:-1][::-1]
        else:
            T = T[:-1]

    return 1 if S == T else 0

S = input().rstrip()
T = input().rstrip()
print(solution(S, T))