tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solution(n, b):
    answer = []
    value = n
    while True:
        if value < b:
            answer.append(str(value))
            break
        answer.append(str(value % b))
        value = value // b
    result = ''
    answer.reverse()
    for val in answer:
        result += tmp[int(val)]
    return result

n, b = map(int, input().split())
print(solution(n, b))