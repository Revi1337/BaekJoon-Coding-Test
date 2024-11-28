def solution(N, students):
    answer = [0] * N
    for idx in range(N):
        answer = answer[:idx - students[idx]] + [idx] + answer[idx - students[idx]:]

    for idx in range(N):
        answer[idx] += 1

    for ans in answer:
        if ans:
            print(ans, end = ' ')
        else:
            break
    print()

N = int(input())
students = list(map(int, input().split()))
solution(N, students)
