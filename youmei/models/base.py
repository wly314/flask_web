# coding:utf-8
import datetime
import sqlalchemy
from sqlalchemy.orm import object_session
from sqlalchemy.ext.declarative import declarative_base
from youmei.config import setting


class tBase(object):
    session = property(lambda self: object_session(self))
    create_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

main_db_info = setting.MAIN_DB
main_db_engine = sqlalchemy.create_engine(
    '%s://%s:%s@%s/%s' % (main_db_info['database_type'], main_db_info['user'],
                            main_db_info['password'], main_db_info['host'],
                            main_db_info['database_name']),
    echo = setting.ECHO_SQL
)

Base = declarative_base(cls=tBase)

metadata = Base.metadata