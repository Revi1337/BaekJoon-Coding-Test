def solution(N):
    cache = [1] * (N + 1)
    for num in range(2, int(N ** 0.5) + 1):
        if cache[num]:
            offset = 2
            while num * offset <= N:
                cache[num * offset] = 0
                offset += 1
    so = [num for num in range(2, N + 1) if cache[num]]

    length = len(so)
    sm = so[0] if so else 0
    answer = right = left = 0
    while left <= right < length:
        if sm >= N:
            if sm == N:
                answer += 1
            sm -= so[left]
            left += 1
        else:
            right += 1
            if right < length:
                sm += so[right]

    return answer

N = int(input())
print(solution(N))