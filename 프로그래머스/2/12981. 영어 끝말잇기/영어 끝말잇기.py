def solution(n, words):
    used = list()
    for idx in range(len(words)):
        stu, turn = idx % n, idx // n
        if not used:
            if len(words[idx]) == 1:
                return [stu + 1, turn + 1]
            used.append(words[idx])
            continue

        if len(words[idx]) == 1 or words[idx] in used or used[-1][-1] != words[idx][0]:
            return [stu + 1, turn + 1]
        used.append(words[idx])

    return [0, 0]