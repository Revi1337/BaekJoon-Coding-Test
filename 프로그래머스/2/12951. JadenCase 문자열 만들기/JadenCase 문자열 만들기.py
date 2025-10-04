def solution(s):
    return " ".join([w.capitalize() for w in s.split(' ')])

print(solution("3people unFollowed me"))
print(solution("for the last week"))
