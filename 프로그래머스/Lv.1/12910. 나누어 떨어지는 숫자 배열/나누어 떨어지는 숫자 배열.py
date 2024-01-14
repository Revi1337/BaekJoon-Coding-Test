def solution(arr, divisor):
    answer = []
    for integer in arr:
        if not integer % divisor:
            answer.append(integer)
    return [-1] if not answer else sorted(answer)