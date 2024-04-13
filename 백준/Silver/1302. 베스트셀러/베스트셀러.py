import sys

input = sys.stdin.readline

def solution(n, books):
    books.sort()
    book_dict = {}
    for book in books:
        book_dict[book] = book_dict.get(book, 0) + 1

    max_count = -float('inf')
    max_book = None
    for book, count in book_dict.items():
        if count > max_count:
            max_count, max_book = count, book

    return max_book


n = int(input().rstrip())
books = [input().rstrip() for _ in range(n)]
print(solution(n, books))
