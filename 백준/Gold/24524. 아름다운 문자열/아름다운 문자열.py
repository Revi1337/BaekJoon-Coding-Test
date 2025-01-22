def solution(S, T):
    dat, T = [[] for _ in range(26)], [ord(char) - 97 for char in T]
    pointer = [0] * 26
    for idx, char in enumerate(S):
        dat[ord(char) - 97].append(idx)


    def binary_search(code_point, cidx):
        left, right = pointer[code_point], len(dat[code_point])
        while left < right:
            mid = (left + right) // 2
            if dat[code_point][mid] <= cidx:
                left = mid + 1
            else:
                right = mid
        return left


    answer = 0
    while True:
        cidx = -1
        for code_point in T:
            pos = binary_search(code_point, cidx)
            if pos == len(dat[code_point]):
                return answer
            cidx = dat[code_point][pos]
            pointer[code_point] = pos + 1

        answer += 1

S = list(input().rstrip())
T = list(input().rstrip())
print(solution(S, T))