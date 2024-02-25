import sys
input = sys.stdin.readline
 
n = int(input())
a = list(range(n))
w = [list(map(int, input().split())) for _ in  range(n)]
 
ans = float('inf')
 
def bf(start,next, cost, visited):
    global ans
    if len(visited)==n:
        tmp = w[next][start]
        if tmp !=0:
            ans = min(ans, cost+tmp)
        return
    
    for i in range(n):
        tmp = w[next][i]
        if tmp!=0 and i not in visited and cost<ans:
            visited.append(i)
            bf(start, i, cost+tmp, visited)
            visited.pop()
        
 
for i in range(n):
    bf(i, i, 0, [i])
print(ans)