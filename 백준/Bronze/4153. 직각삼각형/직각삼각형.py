def solution(triangles):
    for triangle in triangles:
        index = max = 0
        for idx, val in enumerate(triangle):
            if val > max:
                index = idx
                max = val
        triangle.remove(max)
        left = triangle[0] ** 2 + triangle[1] ** 2
        max = max ** 2
        if max == left:
            print('right')
        else:
            print('wrong')

triangles = []
while True:
    data = list(map(int, input().split()))
    if data == [0,0,0]:
        break
    triangles.append(data)

solution(triangles)