def solution(N, S, P):
    player = [set() for _ in range(3)]
    for c in range(N):
        player[P[c]].add(c)

    answer = 0
    visited = set()
    card = list(range(N))
    while True:
        mut_card = tuple(card)
        if mut_card in visited:
            return -1
        visited.add(mut_card)

        allmatch = True
        for idx in range(N):
            if not card[idx] in player[idx % 3]:
                allmatch = False
                break
        if allmatch:
            return answer

        new_card = [0] * N
        for idx in range(N):
            new_card[S[idx]] = card[idx]

        card = new_card
        answer += 1

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))
print(solution(N, S, P))
