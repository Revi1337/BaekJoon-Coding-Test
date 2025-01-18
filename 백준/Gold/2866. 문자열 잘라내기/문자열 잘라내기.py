def solution(R, C, words):
    def is_valid(mid):
        seen = set()
        for col in range(C):
            string = "".join(words[row][col] for row in range(mid, R))
            seen.add(string)
        return len(seen) == C

    answer = 0
    left, right = 0, R
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

R, C = map(int, input().split())
words = [input().rstrip() for _ in range(R)]
print(solution(R, C, words))
