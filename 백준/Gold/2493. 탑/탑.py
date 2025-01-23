'''
# O(N)

0(6) : x -> 6
1(9) : 6 -> pop -> X -> 9
2(5) : 9 -> X -> 갱신 -> 9, 5
3(7) : 9, 5 -> pop -> 갱신 -> 9, 7 
4(4) : 9, 7 -> x -> 갱신 -> 9, 7, 4
'''
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
