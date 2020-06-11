from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.db_models import *

PATH_DB = 'db_test.sqlite3'


class DatabaseConnect:
    def __init__(self, path_db):
        self.engine = create_engine(f'sqlite:///{path_db}?check_same_thread=False')
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session

    def units_create(self, name):
        self.session.add(Units(name))
        self.session.commit()
        return print(f'Добавлена запись: {name}')


if __name__ == '__main__':
    REP = DatabaseConnect(PATH_DB)
    print(Goods.__table__.columns.keys())

