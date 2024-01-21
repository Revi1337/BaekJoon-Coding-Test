def solution(prices):
    answer = []
    length = len(prices)
    for idx in range(length):
        tmp = 0
        for i in range(idx + 1, length):
            tmp += 1
            if prices[idx] > prices[i]:
                break
        answer.append(tmp)
    return answer