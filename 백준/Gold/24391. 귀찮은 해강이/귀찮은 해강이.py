""" O(N + M) """
def solution(N, M, rooms, codes):

    def find(n):
        """ O(1) """
        if parents[n] == n:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        """ O(1) """
        r1, r2 = find(n1), find(n2)
        if r2 > r1:
            parents[r2] = r1
        else:
            parents[r1] = r2

    parents = list(range(N + 1))
    for room1, room2 in rooms: # O(M)
        union(room1, room2)

    answer, prev = 0, find(codes[0])
    for room in codes[1:]: # O(N)
        root = find(room)
        if root != prev:
            answer += 1
        prev = root

    return answer

N, M = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(M)]
codes = list(map(int, input().split()))
print(solution(N, M, rooms, codes))
