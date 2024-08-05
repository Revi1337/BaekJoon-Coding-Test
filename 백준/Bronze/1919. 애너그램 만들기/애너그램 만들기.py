import sys

input = sys.stdin.readline

'''
애너그램 만들기 (https://www.acmicpc.net/problem/1919)
'''

def solution(string1, string2):
    counter1, counter2 = [[0] * 26 for _ in range(2)]
    for char in string1:
        counter1[ord(char) % 26] += 1
    for char in string2:
        counter2[ord(char) % 26] += 1

    answer = 0
    for idx in range(26):
        if counter1[idx] != counter2[idx]:
            answer += max(counter1[idx], counter2[idx]) - min(counter1[idx], counter2[idx])

    return answer

string1 = input().strip()
string2 = input().strip()
print(solution(string1, string2))