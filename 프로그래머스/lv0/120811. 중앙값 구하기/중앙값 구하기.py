def solution(array):
    size = len(array)
    if size == 1:
        return array[0]
    else:
        array.sort()
        if size == 3:
            return array[1]
        else:
            return array[size // 2]
    
    

# def solution(array):
#     lenz = len(array)
#     if lenz == 1:
#         return array[0]
#     else:
#         array.sort()
#         if lenz == 3:
#             return array[1]
#         else:
#             return array[lenz-1//2]
    
    
    