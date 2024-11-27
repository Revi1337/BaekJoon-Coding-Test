def solution(n):
    answer = 0
    for height in range(1, n + 1):
        for width in range(height, n + 1):
            if height * width <= n:
                answer += 1

    return answer

n = int(input())
print(solution(n))