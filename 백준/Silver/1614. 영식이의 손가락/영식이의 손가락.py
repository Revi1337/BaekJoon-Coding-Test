import sys

input = sys.stdin.readline

def solution(N, K):
    answer = 0
    if K == 0:
        if N == 1:
            return 0
        for num in range(1, N + 1):
            if num == N:
                break
            answer += 1
        return answer
    else:
        K -= 1
        answer += 5

        if N == 1:
            if K != 0:
                answer += 8 * K
            for num in range(4, 0, -1):
                if num == N:
                    break
                answer += 1

        elif N == 5:
            if K != 0:
                answer += 8 * K
            answer += 4
            for num in range(2, 6):
                if num == N:
                    break
                answer += 1

        else:
            odd = K % 2
            answer += (4 * K)
            if not odd:
                for num in range(4, 0, -1):
                    if num == N:
                        break
                    answer += 1
            else:
                for num in range(2, 6):
                    if num == N:
                        break
                    answer += 1

    return answer

N = int(input())
K = int(input())
print(solution(N, K))
