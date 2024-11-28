def solution(N, students):
    answer = []
    for idx in range(N):
        answer.insert(students[idx], idx + 1)

    print(*answer[::-1])

N = int(input())
students = list(map(int, input().split()))
solution(N, students)
