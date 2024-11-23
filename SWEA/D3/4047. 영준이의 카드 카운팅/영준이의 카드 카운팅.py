def solution(S):
    cdict = {char: [0] * 14 for char in ['S', 'D', 'H', 'C']}
    for idx in range(0, len(S), 3):
        card = S[idx : idx + 3]
        if cdict[card[0]][int(card[1:])]:
            return 'ERROR'
        cdict[card[0]][int(card[1:])] = 1

    answer = []
    for card in cdict.values():
        answer.append(str(13 - sum(card[1:])))

    return ' '.join(answer)

T = int(input())
for seq in range(T):
    S = input().rstrip()
    print(f'#{seq + 1} {solution(S)}')