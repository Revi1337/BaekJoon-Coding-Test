def solution(want, number, discount):
    table = {}
    for idx in range(len(want)):
        table[want[idx]] = number[idx]

    answer = 0
    for idx in range(len(discount) - 9):
        basket = {}
        for j in range(idx, idx + 10):
            basket.setdefault(discount[j], 0)
            basket[discount[j]] += 1

        boolean = True
        for key in basket:
            if basket.get(key) != table.get(key):
                boolean = boolean and False
                break

        if boolean:
            answer += 1

    return answer