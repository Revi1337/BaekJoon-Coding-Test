def solution(s, n):
    answer = ''
    for char in s:
        if char.isupper():
            padding = (ord(char) - 65 + n) % 26
            answer += chr(65 + padding)
        elif char.islower():
            padding = (ord(char) - 97 + n) % 26
            answer += chr(97 + padding)
        else:
            answer += ' '
    return answer