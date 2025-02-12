def solution(arr1, arr2):  
    arr1_row, arr1_col = len(arr1), len(arr1[1])  
    arr2_col = len(arr2[1])  
    answer = [[0] * arr2_col for _ in range(arr1_row)]  
    for n in range(arr1_row):  
        for k in range(arr2_col):  
            for m in range(arr1_col):  
                answer[n][k] += arr1[n][m] * arr2[m][k]  
    return answer