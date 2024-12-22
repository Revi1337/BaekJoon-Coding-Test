table1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
table2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
com_table = dict(sorted((table1 | table2).items(), key = lambda item: -item[1]))

def solution(str1, str2):
    cost = 0
    for string in str1, str2:
        length = len(string)
        check = [0] * length
        for idx in range(length):
            if not check[idx]:
                if idx + 1 < length and string[idx: idx + 2] in table2:
                    check[idx] = check[idx + 1] = 1
                    cost += table2[string[idx: idx + 2]]
                else:
                    check[idx] = 1
                    cost += table1[string[idx]]

    answer, curr = '', cost
    while curr > 0:
        for key, val in com_table.items():
            if curr >= val:
                answer += key
                curr -= val
                break

    print(cost)
    print(answer)

str1 = input().rstrip()
str2 = input().rstrip()
solution(str1, str2)