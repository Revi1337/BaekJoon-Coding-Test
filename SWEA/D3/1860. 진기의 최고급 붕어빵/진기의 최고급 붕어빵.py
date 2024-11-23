def solution(N, M, K, times):
    times.sort()
    left = 0
    for time in times:
        left += 1
        if (time // M) * K < left:
            return 'Impossible'
    return 'Possible'

T = int(input())
for seq in range(T):
    N, M, K = map(int, input().split())
    humans = list(map(int, input().split()))
    print(f'#{seq + 1} {solution(N, M, K , humans)}')