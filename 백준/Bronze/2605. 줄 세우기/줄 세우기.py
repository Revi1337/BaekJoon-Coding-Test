def solution(N, students):
    answer = []
    for idx in range(N):
        answer = answer[:idx - students[idx]] + [idx] + answer[idx - students[idx]:]

    for idx in range(N):
        answer[idx] += 1

    print(*answer)

N = int(input())
students = list(map(int, input().split()))
solution(N, students)