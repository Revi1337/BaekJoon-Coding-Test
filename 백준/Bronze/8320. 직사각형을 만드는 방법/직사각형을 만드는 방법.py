def solution(n):
    answer = n
    for height in range(2, n):
        count = (n // height) - (height - 1)
        if count < 1:
            break
        answer += count

    return answer

n = int(input())
print(solution(n))