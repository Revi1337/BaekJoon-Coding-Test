def solution(seq, num, cnt):
    lst = list(str(num))
    length = len(lst)
    answer = 0
    check = set()

    def dfs(counter):
        if counter == cnt:
            nonlocal answer
            answer = max(answer, int("".join(map(str, lst))))
            return
        for i in range(length - 1):             # lst 에서 2개를 뽑는 모든 조합 (둘을 교환)
            for j in range(i + 1, length):
                lst[i], lst[j] = lst[j], lst[i]

                tmp = int("".join(map(str, lst)))
                if (counter, tmp) not in check:
                    dfs(counter + 1)
                    check.add((counter, tmp))

                lst[i], lst[j] = lst[j], lst[i] # 반드시 원상복구

    dfs(0)

    return f'#{seq} {answer}'

T = int(input())
for idx in range(T):
    num, cnt = map(int, input().split())
    print(solution(idx + 1, num, cnt))
