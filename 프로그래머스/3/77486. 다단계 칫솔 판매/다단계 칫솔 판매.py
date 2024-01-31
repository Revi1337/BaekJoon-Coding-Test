def solution(enroll, referral, seller, amount):
    mapper = dict(zip(enroll, referral))
    total_dict = {name: 0 for name in enroll}

    for idx in range(len(seller)):
        money = amount[idx] * 100
        cur_name = seller[idx]
        while money > 0 and cur_name != '-':
            total_dict[cur_name] += money - money // 10
            cur_name = mapper[cur_name]
            money //= 10

    return [total_dict[name] for name in enroll]