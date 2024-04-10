import sys

input = sys.stdin.readline

def solution(n, m, arr1, arr2):
    if n <= m:
        book = {value: '' for value in arr2}
        arr = arr1
    else:
        book = {value: '' for value in arr1}
        arr = arr2

    answer = 0
    answer_list = []
    for name in arr:
        if name in book:
            answer += 1
            answer_list.append(name)

    print(answer)
    answer_list.sort()
    for ans in answer_list:
        print(ans)

n, m = map(int, input().split())
arr1 = [input().strip() for _ in range(n)]
arr2 = [input().strip() for _ in range(m)]
solution(n, m, arr1, arr2)