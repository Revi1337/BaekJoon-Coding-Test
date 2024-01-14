def solution(s):
    counter = {}
    s = s.lower()
    for char in s:
        if counter.get(char) is None:
            counter[char] = 0
        else:
            counter[char] += 1
    print(counter)
                
    if counter.get('p') is None and counter.get('y') is None:
        return True
    elif counter.get('p') and counter.get('y'):
        return True if counter.get('p') == counter.get('y') else False
    return False
        