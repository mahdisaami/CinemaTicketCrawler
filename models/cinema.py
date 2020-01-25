from peewee import CharField, TextField
from models.base import BaseModel


class Cinema(BaseModel):
    name = CharField(max_length=32)
    address = TextField()
