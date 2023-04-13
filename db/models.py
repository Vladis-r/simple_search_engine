from sqlalchemy import Column, Integer, Text, String

from db import db


class Data(db.Model):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text, nullable=False)
    rubrics = Column(Text)
    created_date = Column(String(20))
