# coding:utf
import contextlib
from sqlalchemy.orm import sessionmaker
from youmei.models.base import main_db_engine


main_db_session_maker = sessionmaker(bind=main_db_engine)

def get_main_session():
    '''连接到数据库的session'''
    return main_db_session_maker()

@contextlib.contextmanager
def session_cm():
    session = get_main_session()
    try:
        yield session
    except Exception:
        raise
    finally:
        session.close()