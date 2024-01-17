from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from database import District

load_dotenv()
db = os.getenv('DB_ENGINE')
engine = create_engine(db)
Session = sessionmaker(bind=engine)
session = Session()

with open('distr.txt', 'r', encoding='utf-8') as file:

    for line in file:
        district_id, district_name = line.split()
        print(district_id)
        district = District(district_id=int(district_id), district_name=district_name)
        session.add(district)

        session.commit()
        session.close()
