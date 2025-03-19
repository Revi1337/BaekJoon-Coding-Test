def solution(k, dungeons):
    
    def backtracking(n, left, ans):
        if n == length:
            nonlocal answer
            answer = max(answer, ans)
            return
        
        for idx in range(length):
            if not check[idx]:
                check[idx] = 1
                if left >= dungeons[idx][0]:
                    backtracking(n + 1, left - dungeons[idx][1], ans + 1)
                else:
                    backtracking(n + 1, left, ans)
                check[idx] = 0
     
    length = len(dungeons)
    answer = 0
    check = [0] * length
    backtracking(0, k, 0)
    
    return answer