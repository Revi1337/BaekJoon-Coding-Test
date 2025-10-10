def solution(index, num, cnt):

    num_len = len(str(num))
    numbers = list(str(num))
    answer = 0
    check = set()

    def backtracking(change_cnt):
        if change_cnt == cnt:
            nonlocal answer
            answer = max(answer, int("".join(map(str, numbers))))
            return
        for i in range(num_len - 1):
            for j in range(i + 1, num_len):
                numbers[i], numbers[j] = numbers[j], numbers[i]

                chk = int("".join(map(str, numbers)))
                if (change_cnt, chk) not in check:
                    backtracking(change_cnt + 1)
                    check.add((change_cnt, chk))

                numbers[i], numbers[j] = numbers[j], numbers[i]

    backtracking(0)
    return f'#{index} {answer}'

T = int(input())
for index in range(T):
    numbers, cnt = map(int, input().split())
    print(solution(index + 1, numbers, cnt))