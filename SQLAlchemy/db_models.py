from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(25))
    category_desc = Column(String(100))

    def __init__(self, category_name, category_desc):
        self.category_name = category_name
        self.category_desc = category_desc

    def __repr__(self):
        return self.category_name


class Units(Base):
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(String(10))

    def __init__(self, unit_name):
        self.unit_name = unit_name

    def __repr__(self):
        return self.unit_name


class Positions(Base):
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position_name = Column(String(25))

    def __init__(self, position_name):
        self.position_name = position_name

    def __repr__(self):
        return self.position_name


class Goods(Base):
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(25))
    good_unit = ForeignKey(Units.unit_id)

    def __init__(self, good_name, good_unit):
        self.good_name = good_name
        self.good_unit = good_unit

    def __repr__(self):
        return self.good_unit


class Employees(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(25))
    employee_pos = ForeignKey(Positions.position_id)

    def __init__(self, employee_fio, employee_pos):
        self.employee_fio = employee_fio
        self.employee_pos = employee_pos

    def __repr__(self):
        return self.employee_fio


class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(25))
    vendor_ownerchipform = Column(String(50))
    vendor_address = Column(String(200))
    vendor_phone = Column(String(11))
    vendor_email = Column(String(50))

    def __init__(self, vendor_name, vendor_ownerchipform, vendor_address, vendor_phone, vendor_email):
        self.vendor_name = vendor_name
        self.vendor_ownerchipform = vendor_ownerchipform
        self.vendor_address = vendor_address
        self.vendor_phone = vendor_phone
        self.vendor_email = vendor_email

    def __repr__(self):
        return self.vendor_name

