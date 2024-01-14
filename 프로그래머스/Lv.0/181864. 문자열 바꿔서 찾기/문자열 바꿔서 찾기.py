def solution(myString: str, pat:str):
    answer = ""
    for char in myString:
        if char == 'A':
            answer += 'B'
        elif char == 'B':
            answer += 'A'
        else:
            answer += char
    return 1 if pat in answer else 0
