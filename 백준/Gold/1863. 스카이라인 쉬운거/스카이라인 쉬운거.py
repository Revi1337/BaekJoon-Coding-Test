import sys

input = sys.stdin.readline

def solution(N, B):
    ans, stack = 0, []
    for _, h in B:
        while stack and stack[-1] > h:
            stack.pop()
            ans += 1
        if not stack or stack[-1] < h:
            if h > 0:
                stack.append(h)
    ans += len(stack)
    return ans

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, B))
