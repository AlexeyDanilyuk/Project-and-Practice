from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_models import Base, Vendors, Units

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

    def vendors_create(self, *args):
        self.session.add(Vendors(*args[0]))
        self.session.commit()
        return print(f'Добавлена запись: {args[0]}')

    def units_create(self, name):
        self.session.add(Units(name))
        self.session.commit()
        return print(f'Добавлена запись: {name}')


if __name__ == '__main__':
    REP = DatabaseConnect(PATH_DB)
    # Создаем записи в таблице "Поставщики"
    vendors = [
        ('Чернозём', 'ИП', 'Россия', '+74551234561', 'zemlya@russia.ru'),
        ('Мясопродукты', 'ООО', 'Россия', '+74554645645', 'meat@russia.ru'),
    ]
    for i in vendors:
        REP.vendors_create(i)
    # Создаем записи в таблице "Единицы измерения"
    units = ['шт', 'уп', 'кг', 'л', 'м']
    for i in units:
        REP.units_create(i)
