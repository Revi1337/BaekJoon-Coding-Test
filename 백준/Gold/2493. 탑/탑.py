# O(N)
def solution(N, tops):
    stack, answer = [], [0] * N

    for idx, top in enumerate(tops):
        while stack and stack[-1][1] <= top:
            stack.pop()
        if stack:
            answer[idx] = stack[-1][0]
        stack.append((idx + 1, top))

    print(*answer, sep=' ')

N = int(input())
tops = list(map(int, input().split()))
solution(N, tops)