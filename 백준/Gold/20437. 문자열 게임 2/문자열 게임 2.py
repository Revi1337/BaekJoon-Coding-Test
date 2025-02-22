def solution(W, K):
    pos = {}
    for idx, char in enumerate(W):
        pos[char] = pos.get(char, [])
        pos[char].append(idx)

    answer = [1e9, -1]

    for char, indices in pos.items():
        if len(indices) < K:
            continue
        for i in range(len(indices) - K + 1):
            length = indices[i + K - 1] - indices[i] + 1
            answer[0] = min(answer[0], length)
            answer[1] = max(answer[1], length)

    return -1 if answer[1] == -1 else f"{answer[0]} {answer[1]}"

T = int(input())
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    print(solution(W, K))