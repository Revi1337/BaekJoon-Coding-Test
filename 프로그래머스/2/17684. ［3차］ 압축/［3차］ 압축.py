def solution(msg):
    answer = []
    cache = {char: idx for idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start=1)}
    last = 26
    idx = 0
    length = len(msg)
    
    while idx < length:
        best = msg[idx]
        jdx = idx + 1
        
        while jdx <= length and msg[idx:jdx] in cache:
            best = msg[idx:jdx]
            jdx += 1
        answer.append(cache[best])
        
        if jdx <= length:
            last += 1
            cache[msg[idx:jdx]] = last
        
        idx += len(best)

    return answer
