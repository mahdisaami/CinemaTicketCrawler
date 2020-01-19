from peewee import CharField, SmallIntegerField, TimeField, \
    BooleanField

from models.base import BaseModel


class Sans(BaseModel):
    name_saloon = CharField(max_length=32)
    price = SmallIntegerField()
    time = TimeField()
    is_available = BooleanField()
