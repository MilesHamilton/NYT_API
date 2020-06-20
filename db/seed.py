import json

b = open('./popular_books.json')
data = json.load(b)
for books in data['results']:
    print(books)
b.close()
