from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:oybek006@localhost/n75db')

Base = declarative_base()
Session = sessionmaker(bind=engine)

