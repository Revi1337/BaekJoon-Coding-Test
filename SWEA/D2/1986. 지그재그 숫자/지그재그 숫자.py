def solution(T, targets):
    for idx in range(T):
        target = targets[idx]
        psum = [0] * (target + 1)
        for num in range(1, target + 1):
            if num % 2 == 0:
                psum[num] = psum[num - 1] - num
            else:
                psum[num] = psum[num - 1] + num
            if num == target:
                print(f'#{idx + 1} {psum[target]}')

T = int(input())
targets = [int(input()) for _ in range(T)]
solution(T, targets)