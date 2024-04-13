import sys

input = sys.stdin.readline

def solution(n, files):
    file_dict = {}
    for file in files:
        extension = file.split('.')[1]
        file_dict[extension] = file_dict.get(extension, 0) + 1

    sorted_extension = sorted(file_dict.keys())
    for ext in sorted_extension:
        print(f'{ext} {file_dict[ext]}')

n = int(input().rstrip())
files = [input().strip() for _ in range(n)]
solution(n, files)