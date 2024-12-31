def solution(H, W, waters):
    answer = 0
    while sum(waters) > 0:
        before, cnt = False, 0
        for col in range(W):
            if waters[col] :
                before = True
                answer += cnt
                cnt = 0
            else:
                if before:
                    cnt += 1

        for col in range(W):
            waters[col] = max(0, waters[col] - 1)

    return answer

H, W = map(int, input().split())
waters = list(map(int, input().split()))
print(solution(H, W, waters))
