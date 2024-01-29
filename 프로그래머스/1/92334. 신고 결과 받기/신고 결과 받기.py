def solution(id_list, report, k):
    reported_dict = {}
    for content in report:
        user_id, reported_id = content.split()
        if reported_id not in reported_dict:
            reported_dict[reported_id] = set()
        reported_dict[reported_id].add(user_id)

    reported_counter = {}
    for _, user_ids in reported_dict.items():
        if len(user_ids) >= k:
            for user_id in user_ids:
                if user_id not in reported_counter:
                    reported_counter[user_id] = 1
                else:
                    reported_counter[user_id] += 1

    answer = []
    for idx in range(len(id_list)):
        if id_list[idx] not in reported_counter:
            answer.append(0)
        else:
            answer.append(reported_counter[id_list[idx]])
    return answer