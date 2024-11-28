def solution(stu):
    answer = 0
    for i in range(1, 20):
        for j in range(i):
            if stu[i] < stu[j]:
                answer += 1

    return answer

T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    seq = data[0]
    stu = data[1:]
    print(f'{seq} {solution(stu)}')