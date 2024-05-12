def solution(T, target):
    answer = [0] * 10
    offset = 1
    while True:
        for char in str(target * offset):
            answer[int(char)] = 1
        if sum(answer) == 10:
            break
        offset += 1
    return f'#{T} {target * offset}'
 
T = int(input())
for idx in range(T):
    target = int(input())
    print(solution(idx + 1, target))