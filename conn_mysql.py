from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_sqlalch import Device1, Base

try:
    engine = create_engine('mysql+pymysql://sabry:password123@localhost:3306')
    engine.execute("USE mydbt1")

except Exception as e:
    print("Error during connection: ", str(e))

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

device1 = Device1(ipAddress="172.16.1.1", port="3332")
device2 = Device1(ipAddress="192.168.1.1", port="1111")
l = [device1,device2]

for i in l:
    session.add(i)

session.commit()