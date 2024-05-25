import sys

open = sys.stdin.readline

def solution(string):
    # 각 알파벳 빈도수 조회(왜 dict 를 안썻나? --> 배열로 풀고 싶었음.)
    frequency = [0] * 26
    for char in string:
        frequency[(ord(char) - 65) % 26] += 1

    # 빈도수가 홀수개인 알파벳이 2개 이상이면 펠린드롬을 만들수가 없음 && 빈도수가 홀수개의 알파벳을 찾는다.
    odd_cnt = 0
    odd_char = ""
    for idx in range(26):
        if frequency[idx] % 2:
            odd_cnt += 1
            if odd_cnt > 1:
                return 'I\'m Sorry Hansoo'
            odd_idx = idx
            odd_char = chr(odd_idx + 65)

    # 펠린드롬의 절반을 만들어줌.
    half = ""
    for idx in range(26):
        if frequency[idx]:
            half += chr(idx + 65) * (frequency[idx] // 2)

    # 빈도수가 홀수개인 알파벳이 존재하면, (절반 + 홀수 알파벳 + rev(절반))
    if odd_char:
        return half + odd_char + half[::-1]
    # 빈도수가 홀수개인 알파벳이 존재하면, (절반 + rev(절반))
    return half + half[::-1]

string = input().rstrip()
print(solution(string))
