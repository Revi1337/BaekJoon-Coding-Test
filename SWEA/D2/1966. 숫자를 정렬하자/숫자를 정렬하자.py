def solution(T, numbers):
    print(f'#{T}', end = ' ')
    print(*sorted(numbers))

T = int(input())
for idx in range(T):
    length = int(input())
    numbers = list(map(int, input().split()))
    solution(idx + 1, numbers)