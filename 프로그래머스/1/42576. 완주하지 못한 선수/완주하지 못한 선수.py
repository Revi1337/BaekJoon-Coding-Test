def solution(participant, completion):
    compl_dict = {}
    for compl in completion:
        compl_dict[compl] = compl_dict.get(compl, 0) + 1
    for par in participant:
        if par not in compl_dict:
            return par

        compl_dict[par] -= 1
        
        if compl_dict[par] < 0:
            return par