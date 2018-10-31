from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from createdb import Base, Employee, Address
engine = create_engine('sqlite:///employeeData.db')
# bind engine to base class
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()