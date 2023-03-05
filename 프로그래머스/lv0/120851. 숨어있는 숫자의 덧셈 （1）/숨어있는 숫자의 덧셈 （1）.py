def solution(my_string):
    return sum(map(int, filter(lambda x:x.isnumeric(), my_string)))