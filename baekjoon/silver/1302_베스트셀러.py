from collections import Counter
from sys import stdin

input = stdin.readline

N = int(input())
books = [input().strip() for _ in range(N)]


book_counts = Counter(books)
max_count = max(book_counts.values())

most_frequent_books = [book for book,
                       count in book_counts.items() if count == max_count]
most_frequent_books.sort()

print(most_frequent_books[0])
