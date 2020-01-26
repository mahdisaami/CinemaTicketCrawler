from peewee import CharField, TextField
from models.base import BaseModel


class Cinema(BaseModel):
    name = CharField()
    address = TextField()
