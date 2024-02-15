
from peewee import *


db = SqliteDatabase('driver.db')


class BaseModel(Model):

    class Meta:
        database = db


class Driver(BaseModel):
    id = PrimaryKeyField(unique=True)
    name = CharField()
    team = CharField()
    result_time = TimeField()


Driver.create_table()
