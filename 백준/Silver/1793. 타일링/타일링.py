def solution(arr):
    mx = max(arr)
    dp = [1] * (mx + 1)
    for num in range(2, mx + 1):
        dp[num] = dp[num - 1] + dp[num - 2] * 2

    print(*[dp[num] for num in arr], sep = '\n')

lst = []
while True:
    try:
        string = input()
        lst.append(int(string))
    except Exception:
        solution(lst)
        break
