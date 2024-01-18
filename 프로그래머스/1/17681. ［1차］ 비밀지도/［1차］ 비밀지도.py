def solution(n, arr1, arr2):
    answer = []
    for idx in range(n):
        v1 = arr1[idx]
        v2 = arr2[idx]
        bits = f'{str(bin(v1 | v2))[2:]:0>{n}}'
        answer.append("".join(['#' if int(bit) else ' ' for bit in bits]))
    return answer