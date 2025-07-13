def solution(N, classes, B, C):
    ans = 0
    for cla in classes:
        ans += 1
        cla -= B
        if cla > 0:
            if cla < C:
                ans += 1
            elif cla % C:
                ans += (cla // C) + 1
            else:
                ans += cla // C

    return ans

N = int(input())
classes = list(map(int, input().split()))
B, C = map(int, input().split())
print(solution(N, classes, B, C))