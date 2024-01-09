from collections import defaultdict

def solution(X, Y):
    answer = ''
    x = defaultdict(int)
    y = defaultdict(int)
    for char in X:
        x[char] += 1
    for char in Y:
        y[char] += 1

    if len(X) <= len(Y):
        string = X
    else:
        string = Y

    for integer in string:
        if x.get(integer) is None or y.get(integer) is None:
            continue
        if x[integer] == 0 or y[integer] == 0:
            continue
        x[integer] -= 1
        y[integer] -= 1
        answer += integer

    if not answer:
        return '-1'
    elif answer == ('0' * len(answer)):
        return '0'
    else:
        return "".join(sorted(answer, reverse=True))