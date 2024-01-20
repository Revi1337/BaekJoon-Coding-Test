def solution(participant, completion):
    table = {}
    for person in participant:
        table.setdefault(person, 0)
        table[person] += 1
    for compl in completion:
        table[compl] -= 1
    for key, value in table.items():
        if value == 1:
            return key