def solution(S):
    counter = [int(S[0] == '0'), int(S[0] == '1')]
    for idx in range(1, len(S)):
        if S[idx] == '1' and S[idx] != S[idx - 1]:
            counter[1] += 1
        if S[idx] == '0' and S[idx] != S[idx - 1]:
            counter[0] += 1

    return min(counter)

S = input().rstrip()
print(solution(S))