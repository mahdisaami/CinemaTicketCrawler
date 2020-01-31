from peewee import CharField, TimeField, \
    BooleanField, DateField

from models.base import BaseModel


class Sans(BaseModel):
    date = DateField(null=True)
    name_saloon = CharField(null=True)
    price = CharField(null=True)
    time = TimeField(null=True)
    is_available = BooleanField(null=True)
    url = CharField(null=True)
