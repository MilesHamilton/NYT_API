from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
# from typing import Iterator, Dict, Any, get

db = PostgresqlDatabase('books', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Books(BaseModel):
    title = CharField()
    description = CharField(null=True)
    author = CharField()


db.connect()
db.drop_tables([Books])
db.create_tables([Books])

b = open('../popular_books.json')
data = json.load(b)
for books in data['results']:
    print(books)
# b.close()

with db.atomic():
    Books.insert_many(data['results'], fields=[
                      Books.title, Books.description, Books.author]).execute()

print('success')
