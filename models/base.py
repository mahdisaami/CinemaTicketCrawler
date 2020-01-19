from datetime import datetime

from config import connect_mysql
from peewee import Model, DateTimeField


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())
    modified_time = DateTimeField(default=datetime.now())

    class Meta:
        database = connect_mysql()

    def save(self, force_insert=False, only=None):
        self.modified_time = datetime.now()
        return super().save(force_insert, only)
