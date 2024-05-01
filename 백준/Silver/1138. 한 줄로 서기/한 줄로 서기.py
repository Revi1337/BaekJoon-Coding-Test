import sys

input = sys.stdin.readline

def solution(N, a):
    answer = [0] * N
    for i in range(N):
        counter = 0
        for idx in range(N):
            if counter == a[i] and answer[idx] == 0:
                answer[idx] = i + 1
                break
            elif answer[idx] == 0:
                counter += 1
    print(*answer)

N = int(input().rstrip())
a = list(map(int, input().split()))
solution(N, a)
