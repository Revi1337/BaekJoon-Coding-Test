import sys

input = sys.stdin.readline

'''
걸그룹 마스터 준석이 (https://www.acmicpc.net/problem/16165)
'''

def solution(N, M, groups, quiz):
    gdict = {}
    members = {}
    for group in groups:
        gdict[group[0]] = []
        for mem in group[1:]:
            gdict[group[0]].append(mem)
            members[mem] = group[0]

    for data, type in quiz:
        if type:
            print(members[data])
        else:
            for mem in sorted(gdict[data]):
                print(mem)

N, M = map(int, input().split())
groups = []
quiz = []
for _ in range(N):
    group = input().rstrip()
    count = int(input())
    data = [group]
    for _ in range(count):
        data.append(input().rstrip())
    groups.append(data)
for _ in range(M):
    q = [input().rstrip(), int(input())]
    quiz.append(q)
solution(N, M, groups, quiz)

