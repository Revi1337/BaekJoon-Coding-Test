def solution(n):
    tmp = ""
    while n >= 3:
        tmp += str(n % 3)
        n //= 3
    tmp += str(n)
    tmp = tmp[::-1]
    print(tmp)

    answer = 0
    for idx in range(len(tmp)):
        answer += int(tmp[idx]) * (3 ** idx)
    return answer