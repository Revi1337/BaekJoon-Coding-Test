def solution(today, terms, privacies):
    tyear, tmon, tday = map(int, today.split('.'))
    ttime = (28 * 12 * tyear) + (28 * tmon) + tday
    
    policies = {}
    for term in terms:
        kind, exp = term.split()
        policies[kind] = exp 
    
    answer = []
    for idx in range(len(privacies)):
        year, mon, day = map(int, privacies[idx][:-2].split('.'))
        durable = int(policies[privacies[idx][-1]])
        
        time = (28 * 12 * year) + (28 * mon) + day
        time += (28 * durable) - 1
        
        if time < ttime:
            answer.append(idx + 1)
        
        
    return answer
