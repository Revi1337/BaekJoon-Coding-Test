def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want, number))
    for padding in range(len(discount) - 9):
        wish = {}
        for day in range(padding, padding + 10):
            wish[discount[day]] = wish.get(discount[day], 0) + 1
        if wish == want_dict:
            answer += 1
    return answer