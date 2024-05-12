def solution(T, P, Q, R, S, W):
    answer = [0] * 2
    answer[0] = P * W
    if W >= R:
        answer[1] = Q + ((W - R) * S)
    elif R > W:
        answer[1] = Q
    return f'#{T} {min(answer)}'
 
T = int(input())
for idx in range(T):
    P, Q, R, S, W = map(int, input().split())
    print(solution(idx + 1, P, Q, R, S, W))