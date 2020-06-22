from peewee import *
from seed import data

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

with db.atomic():
    Books.insert_many(data['results'], fields=[
                      Books.title, Books.description, Books.author]).execute()

print('success')
