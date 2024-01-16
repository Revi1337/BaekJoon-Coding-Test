def solution(d, budget):
    answer = 0
    d.sort()
    sumN = 0
    for stock in d:
        if budget >= (sumN + stock):
            sumN += stock
            answer += 1
    return answer