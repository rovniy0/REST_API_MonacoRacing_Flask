
from peewee import *

db = SqliteDatabase('driver.db')


class Driver(Model):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    team = CharField()
    result_time = TimeField()

