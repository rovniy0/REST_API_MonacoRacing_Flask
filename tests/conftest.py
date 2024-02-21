
import pytest

from report_racing_app import app
from peewee import SqliteDatabase
from report_racing_app.models import Driver


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def db():
    test_db = SqliteDatabase(':memory:')
    Driver.database = test_db
    test_db.create_tables([Driver])
    Driver.create(id='SVF', name='Sebastian Vettel', team='FERRARI', result_time='0:01:04.415000')
    yield test_db
    test_db.drop_tables([Driver])
