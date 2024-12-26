def solution(K, signs):

    def backtracking(n, num, strings):
        if n == K + 1:
            nonlocal ans1, ans2
            value = int("".join(strings))
            ans1, ans2 = max(ans1, value), min(ans2, value)
            return

        curr_sign = signs[n - 1]
        for integer in range(10):
            if not check[integer]:
                if curr_sign == '>':
                    if num > integer:
                        check[integer] = 1
                        backtracking(n + 1, integer, strings + [str(integer)])
                        check[integer] = 0
                else:
                    if num < integer:
                        check[integer] = 1
                        backtracking(n + 1, integer, strings + [str(integer)])
                        check[integer] = 0

    INF = float('inf')
    ans1, ans2 = -INF, INF
    check = [0] * 10
    for num in range(10):
        check[num] = 1
        backtracking(1, num, [str(num)])
        check[num] = 0

    print(f'{ans1:0{K + 1}}')
    print(f'{ans2:0{K + 1}}')


K = int(input())
signs = list(input().rstrip().split())
solution(K, signs)