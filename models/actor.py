from peewee import CharField

from models.base import BaseModel


class Actor(BaseModel):
    name = CharField(max_length=32)
