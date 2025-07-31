import sys

input = sys.stdin.readline

def solution(N, L, arr):

    reverse = lambda x: list(map(list, zip(*x)))

    def process(arr):
        ans = 0
        for row in range(N):
            check = [0] * N
            for col in range(1, N):
                diff = arr[row][col] - arr[row][col - 1]
                if diff == 0:
                    continue

                elif diff == 1:
                    if col - L < 0:
                        break
                    for k in range(col - L, col):
                        if arr[row][k] != arr[row][col - 1] or check[k]:
                            break
                    else:
                        for k in range(col - L, col):
                            check[k] = 1
                        continue
                    break

                elif diff == -1:
                    if col + L - 1 >= N:
                        break
                    for k in range(col, col + L):
                        if arr[row][k] != arr[row][col] or check[k]:
                            break
                    else:
                        for k in range(col, col + L):
                            check[k] = 1
                        continue
                    break

                else:
                    break
            else:
                ans += 1

        return ans

    ans = 0
    ans += process(arr)
    ans += process(reverse(arr))

    return ans

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, L, arr))