from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

Base = declarative_base()
load_dotenv()


class District(Base):
    __tablename__ = 'District'

    district_id = Column(Integer, unique=True, primary_key=True)
    district_name = Column(String)


db = os.getenv('DB_ENGINE')
engine = create_engine(db)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
