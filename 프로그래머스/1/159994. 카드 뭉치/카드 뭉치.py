def solution(cards1, cards2, goal):
    card1_idx, card2_idx = 0, 0
    for word in goal:
        if len(cards1) > card1_idx and word == cards1[card1_idx]:
            card1_idx += 1
        elif len(cards2) > card2_idx and word == cards2[card2_idx]:
            card2_idx += 1
        else:
            return 'No'
    return 'Yes'