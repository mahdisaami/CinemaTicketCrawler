from peewee import CharField, SmallIntegerField, TimeField, \
    BooleanField

from models.base import BaseModel


class Sans(BaseModel):
    name_saloon = CharField()
    price = SmallIntegerField()
    time = TimeField()
    is_available = BooleanField()
