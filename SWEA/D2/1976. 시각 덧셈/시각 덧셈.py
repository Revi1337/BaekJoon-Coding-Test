def solution(idx, times):
    h1, m1, h2, m2 = times
    m = m1 + m2 + (h1 * 60) + (h2 * 60)
    hour, minute = divmod(m, 60)
    return f'#{idx} {12 if hour % 12 == 0 else hour % 12} {minute}'

T = int(input())
for idx in range(T):
    times = list(map(int, input().split()))
    print(solution(idx + 1, times))
