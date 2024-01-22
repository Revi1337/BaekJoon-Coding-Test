keypad = [
    [3,1],[0,0],[0,1],[0,2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2],
    [3, 0], [3, 1], [3, 2]
]

def solution(numbers, hand):
    answer = ''
    button = [[]]
    left = [3,0]
    right = [3,2]
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            left = keypad[number]
        elif number in [3,6,9]:
            answer += 'R'
            right = keypad[number]
        elif number in [2,5,8,0]:
            distanceL = abs(keypad[number][0] - left[0]) + abs(keypad[number][1] - left[1])
            distanceR = abs(keypad[number][0] - right[0]) + abs(keypad[number][1] - right[1])
            if distanceL > distanceR:
                answer += 'R'
                right = keypad[number]
            elif distanceL < distanceR:
                answer += 'L'
                left = keypad[number]
            elif distanceL == distanceR:
                if hand == 'right':
                    answer += 'R'
                    right = keypad[number]
                else:
                    answer += 'L'
                    left = keypad[number]
    return answer