def solution(s, skip, index):
    answer = ''
    for c in s:
        i = ord(c)
        j = index
        while j > 0:
            i += 1
            if i > 122:
                i = 97
            if chr(i) in skip:
                j += 1
            j -= 1
        answer += chr(i)
    
    return answer