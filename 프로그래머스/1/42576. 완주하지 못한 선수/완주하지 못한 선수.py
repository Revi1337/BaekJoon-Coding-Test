def solution(participant, completion):
    table = {}
    for human in participant:
        table.setdefault(human, 0)
        table[human] += 1
    for com in completion:
        if com in table:
            table[com] -= 1
    for key in table:
        if table[key] > 0:
            return key