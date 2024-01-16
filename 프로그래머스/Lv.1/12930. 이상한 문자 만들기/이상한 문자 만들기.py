def solution(s):
    answer = []
    words = s.split(' ')
    for word in words:
        tmp = ''
        for idx in range(len(word)):
            if idx % 2:
                tmp += word[idx].lower()
            else:
                tmp += word[idx].upper()
        answer.append(tmp)
    return ' '.join(answer)