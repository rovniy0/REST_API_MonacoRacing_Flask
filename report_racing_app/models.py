
from peewee import *


db = SqliteDatabase('driver.db')


class BaseModel(Model):

    class Meta:
        database = db


class Driver(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    team = CharField()
    result_time = CharField()

    class Meta:
        db_table = 'drivers'


Driver.create_table()
