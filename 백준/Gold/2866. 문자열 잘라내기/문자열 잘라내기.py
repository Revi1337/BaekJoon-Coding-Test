def solution(R, C, words):
    
    def is_valid(mid):
        cache = set()
        for col in range(C):
            string = "".join(words[row][col] for row in range(mid, R))
            if string in cache:
                return False
            cache.add(string)
        return True

    answer = 0
    left, right = 0, R - 1
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

