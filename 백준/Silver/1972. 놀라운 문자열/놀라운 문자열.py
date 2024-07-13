import sys

input = sys.stdin.readline

def solution(datas):
    for string in datas:
        length = len(string)
        offset = length - 2
        uniq = True
        for off in range(1, offset + 1):
            judge = set()
            curr_uniq = True
            for idx in range(length):
                if idx + off + 1 <= length:
                    pre = string[idx : idx + off + 1 : off]
                    if pre in judge:
                        curr_uniq = False
                        break
                    judge.add(pre)
            if not curr_uniq:
                uniq = False
                break
        if not uniq:
            print(f'{string} is NOT surprising.')
        else:
            print(f'{string} is surprising.')

datas = []
while True:
    data = input().strip()
    if data == '*':
        solution(datas)
        break
    datas.append(data)

