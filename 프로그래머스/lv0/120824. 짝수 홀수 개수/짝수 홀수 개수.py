def solution(num_list):
    pre = len(list(filter(lambda x: x%2 == 0, num_list)))
    return [pre, len(num_list) - pre]