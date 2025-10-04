def solution(arr1, arr2):
    arr1.sort()
    arr2.sort(reverse=True)

    return sum(arr1[idx] * arr2[idx] for idx in range(len(arr1)))