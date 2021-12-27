from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = 'root'
PASSWORD = ''
HOST = 'localhost'
BD = 'sistemaLogin'
PORT = '3306'

URL_CONNECTION = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{BD}'

ENGINE = create_engine(URL_CONNECTION, echo=True)
Session = sessionmaker(bind=ENGINE)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(200))
    password = Column(String(100))

Base.metadata.create_all(ENGINE)
