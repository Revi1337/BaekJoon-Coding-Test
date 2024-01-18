words = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solution(s):
    answer = ''
    stack = []
    tmp = ''
    for char in s:
        if char.isdigit():
            answer += char
            continue
        tmp += char
        if tmp in words:
            answer += words[tmp]
            tmp = ''
    return int(answer)