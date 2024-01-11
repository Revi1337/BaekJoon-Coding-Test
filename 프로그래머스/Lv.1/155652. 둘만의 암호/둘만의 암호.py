def solution(s, skip, index):
    answer = ''
    for char in s:
        ascii = ord(char)
        seq = index
        while seq > 0:
            ascii += 1
            if ascii > 122:
                ascii = 97
            if chr(ascii) in skip:
                seq += 1
            seq -= 1
        answer += chr(ascii)
    return answer

print(solution("aukks",	"wbqd",	5))

