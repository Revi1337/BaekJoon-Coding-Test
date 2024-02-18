def solution(phone_book):
    answer = True
    table = {}
    for phone in phone_book:
        table[phone] = 1
    for phone in phone_book:
        tmp = ''
        for integer in phone:
            tmp += integer
            if tmp in table and tmp != phone:
                answer = False
                break
    return answer