def solution(numbers, target):

    
    def dfs(n, sm):
        if n == length:
            if sm == target:
                nonlocal answer
                answer += 1
            return
        
        dfs(n + 1, sm + numbers[n])
        dfs(n + 1, sm - numbers[n])
        
    
    length = len(numbers)
    answer = 0
    dfs(0, 0)
    
    return answer