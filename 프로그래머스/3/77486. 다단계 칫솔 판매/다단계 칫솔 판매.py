def solution(enroll, referral, seller, amount):
    recommend_dict = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}

    for idx in range(len(seller)):
        price = amount[idx] * 100
        celler = seller[idx]
        while celler != '-' and price > 0:
            total[celler] += price - price // 10
            celler = recommend_dict[celler]
            price //= 10

    return [total[name] for name in enroll]