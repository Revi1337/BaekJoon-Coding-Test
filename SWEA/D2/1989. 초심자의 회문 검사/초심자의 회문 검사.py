def solution(T, word):
    reverse_word = word[::-1]
    if reverse_word == word:
        return f'#{T} 1'
    return f'#{T} 0'
 
T = int(input())
for idx in range(T):
    word = input().rstrip()
    print(solution(idx + 1, word))