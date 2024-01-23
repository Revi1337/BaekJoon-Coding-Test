from collections import deque

def solution(cards1, cards2, goal):
    answer = 'Yes'
    queue = deque(goal)
    cards1_idx = cards2_idx = 0
    cards1_length, cards2_length = len(cards1), len(cards2)
    while queue:
        expect = queue.popleft()
        if cards1_length > cards1_idx and cards1[cards1_idx] == expect:
            cards1_idx += 1
        elif cards2_length > cards2_idx and cards2[cards2_idx] == expect:
            cards2_idx += 1
        else:
            return 'No'
    return answer