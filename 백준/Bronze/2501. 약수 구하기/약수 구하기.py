def solution(num, th):
    answer = []
    for val in range(1, num + 1):
        if num % val == 0:
            answer.append(val)
    length = len(answer)
    if th - 1 >= length:
        return 0
    return answer[th - 1]

num, th = map(int, input().split())
print(solution(num, th))