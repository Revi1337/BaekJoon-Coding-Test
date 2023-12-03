def solution(m, n):
    answer = []
    for num in range(m, n + 1):
        cnt = 0
        if num > 1:
            for val in range(2, int(num * 0.5) + 1):
                if num % val == 0:
                    cnt += 1
                    break
            if cnt == 0:
                answer.append(num)
    if len(answer) == 0:
        print(-1)
        return
    print(sum(answer))
    print(answer[0])


m = int(input())
n = int(input())
solution(m, n)
