def solution(string1, string2):
    dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
    for idx in range(1, len(string1) + 1):
        for jdx in range(1, len(string2) + 1):
            if string1[idx - 1] == string2[jdx - 1]:
                dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1
            else:
                dp[idx][jdx] = max(dp[idx - 1][jdx], dp[idx][jdx - 1])

    return dp[-1][-1]

string1 = input().rstrip()
string2 = input().rstrip()
print(solution(string1, string2))

