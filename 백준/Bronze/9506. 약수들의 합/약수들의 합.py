def solution(number):
    answer = []
    for val in range(1, number // 2 + 1):
        if number % val == 0:
            answer.append(val)
    if sum(answer) == number:
        return f"{number} = {' + '.join(map(str, answer))}"
    else:
        return f"{number} is NOT perfect."

while True:
    data = int(input())
    if data == -1:
        break
    print(solution(data))