from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from class_sqlalch import Device, Base

try:
    engine = create_engine('mysql+pymysql://sabry:password123@localhost:3306')
    engine.execute("USE mydbt1")

except Exception as e:
    print("Error during connection: ", str(e))

Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

device1 = Device(ipAddress="172.16.1.1", port="3332")
device2 = Device(ipAddress="10.10.10.1", port="8080")
device3 = Device(ipAddress="192.168.30.101", port="1111")

l = [device1, device2, device3]

for i in l:
    session.add(i)

session.commit()