def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    return [sorted_emergency.index(score) + 1 for score in emergency]