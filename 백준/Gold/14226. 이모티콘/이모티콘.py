from collections import deque
import sys

input = sys.stdin.readline

"""
이미 (현재 화면, 클립보드) 가 check 에 들어있다면 무시할 수 있음
    - 왜? 후에 들어온 튜플은 당연히 시간히 더 오래 걸린것이기 때문 
"""
def solution(s):
    check = dict()
    check[(1, 0)] = 0
    queue = deque([(1, 0)])
    while queue:
        screen, cache = queue.popleft()
        if screen == s:
            return check[(screen, cache)]
        if (screen, screen) not in check.keys():                    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장했을 때
            check[(screen, screen)] = check[(screen, cache)] + 1
            queue.append((screen, screen))
        if (screen + cache, cache) not in check.keys():             # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기했을 때
            check[(screen + cache, cache)] = check[(screen, cache)] + 1
            queue.append((screen + cache, cache))
        if (screen - 1, cache) not in check.keys():                 # 화면에 있는 이모티콘 중 하나를 삭제했을 때
            check[(screen - 1, cache)] = check[(screen, cache)] + 1
            queue.append((screen - 1, cache))

s = int(input())
print(solution(s))
