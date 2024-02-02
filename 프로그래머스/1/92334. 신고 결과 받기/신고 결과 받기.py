def solution(id_list, report, k):
    reported_dict = {}
    for string in report:
        report_user, reported_user = string.split()
        reported_dict[reported_user] = reported_dict.get(reported_user, set())
        reported_dict[reported_user].add(report_user)

    id_length = len(id_list)
    answer = [0] * id_length
    for reported_user in reported_dict:
        report_users = reported_dict[reported_user]
        if len(report_users) >= k:
            for idx in range(id_length):
                user_id = id_list[idx]
                if user_id in report_users:
                    answer[idx] += 1
    return answer