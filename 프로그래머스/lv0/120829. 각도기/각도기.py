def solution(angle):
    if 0 < angle < 90: 
        res=1
    elif angle == 90:
        res=2
    elif 90 < angle < 180:
        res=3 
    else:
        res=4
    return res