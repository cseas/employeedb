from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from createdb import Base, Employee, Address
engine = create_engine('sqlite:///employeeData.db')
# bind engine to base class
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

newEmployee = Employee(name="Rebecca Allen")
session.add(newEmployee)
session.commit()

rebeccaAddress = Address(
    street="512 Sycamore Road",
    zip="02001",
    employee=newEmployee)
session.add(rebeccaAddress)
session.commit()