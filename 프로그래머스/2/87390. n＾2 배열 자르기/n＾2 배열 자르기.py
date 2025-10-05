def solution(n, left, right):
    ans = []
    for p in range(left, right + 1):
        row, col = divmod(p, n)
        ans.append(max(row, col) + 1)

    return ans