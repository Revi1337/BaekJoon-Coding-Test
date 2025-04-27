def solution(N, numbers):

    def insert(dic, number):
        if not len(number):
            return

        if number[0] not in dic:
            dic[number[0]] = {}
        insert(dic[number[0]], number[1:])

    def search(dic, number):
        if not number:
            return True
        if number[0] not in dic:
            return True
        if not dic[number[0]]:
            return False
        return search(dic[number[0]], number[1:])

    trie = {}
    numbers.sort(key = lambda x: len(x))
    for number in numbers:
        number = str(number)
        if not search(trie, number):
            return 'NO'
        insert(trie, number)
    return 'YES'

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    print(solution(n, numbers))