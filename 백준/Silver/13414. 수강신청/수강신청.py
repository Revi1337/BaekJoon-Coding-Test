import sys

input = sys.stdin.readline

def solution(k, l, lst):
    dictionary = {}
    for number in lst:
        if number in dictionary:
            dictionary.pop(number)
        dictionary[number] = ''

    counter = k
    for number in dictionary:
        if counter == 0:
            break
        print(number)
        counter -= 1

k, l = map(int, input().split())
lst = [input().strip() for _ in range(l)]
solution(k, l, lst)