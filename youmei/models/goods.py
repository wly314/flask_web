# coding:utf-8
from datetime import datetime
from youmei.models.session import session_cm
from youmei.models.base import Base
import sqlalchemy as SA
from sqlalchemy.dialects.postgresql import INTEGER, TEXT

class Goods(Base):
    '''货源商品表'''
    __tablename__ = 'goods'

    id = SA.Column(INTEGER, primary_key=True)
    name = SA.Column(TEXT, index=True)

    @staticmethod
    def to_json(goods):
        data = []
        return data


