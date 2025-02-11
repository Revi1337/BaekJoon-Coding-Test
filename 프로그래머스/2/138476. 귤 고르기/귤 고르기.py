def solution(k, tangerine):
    pre = {}
    for gul in tangerine:
        pre[gul] = pre.get(gul, 0) + 1
    
    table = {}
    for gul, cnt in pre.items():
        table[cnt] = table.get(cnt, [])
        table[cnt].append(gul)
        
    answer = 0
    counted = sorted(table, reverse=True)
    for cnt in counted:
        for _ in table[cnt]:
            k -= cnt
            answer += 1
            if k <= 0:
                return answer
                
    return answer
