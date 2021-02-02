from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from class_sqlalch import Device1, Base


try:
    engine = create_engine('mysql+pymysql://sabry:password123@localhost:3306/mydbt1')
    
except Exception as e:
    print("Error during connection: ", str(e))

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
