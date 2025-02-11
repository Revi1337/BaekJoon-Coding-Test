def solution(k, tangerine):
    pre = {}
    for gul in tangerine:
        pre[gul] = pre.get(gul, 0) + 1
    
    table = {}
    for gul, cnt in pre.items():
        table[cnt] = table.get(cnt, [])
        table[cnt].append(gul)
        
    answer = total = 0
    counted = sorted(table, reverse = True)
    for cnt in counted:
        kinds = table[cnt]
        for _ in kinds:
            total += cnt
            answer += 1
            if total >= k:
                return answer
