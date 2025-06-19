def solution(S):
    counter = [0, 0]
    for i in range(1, len(S)):
        if S[i] == '0' and S[i - 1] == '1':
            counter[0] += 1
        if S[i] == '1' and S[i - 1] == '0':
            counter[1] += 1
    if S[0] == '0':
        counter[0] += 1
    if S[0] == '1':
        counter[1] += 1

    return min(counter)

S = input().rstrip()
print(solution(S))