def solution(N, arr1, M, arr2):
    common = set(arr1) & set(arr2)
    if not common:
        print(0)
        return

    ans = []
    while common:
        mx  = max(common)
        ans.append(mx)

        idx1, idx2 = arr1.index(mx), arr2.index(mx)
        arr1, arr2 = arr1[idx1 + 1:], arr2[idx2 + 1:]
        common = set(arr1) & set(arr2)

    print(len(ans))
    print(*ans)

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
solution(N, arr1, M, arr2)
