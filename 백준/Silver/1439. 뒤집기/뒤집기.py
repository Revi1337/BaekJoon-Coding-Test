def solution(S):
    counter = [0, 0]
    flag0 = flag1 = False
    for ch in S:
        if ch == '0':
            flag1 = False
            if not flag0:
                counter[0] += 1
                flag0 = True
        else:
            flag0 = False
            if not flag1:
                counter[1] += 1
                flag1 = True

    return min(counter)

S = input().rstrip()
print(solution(S))