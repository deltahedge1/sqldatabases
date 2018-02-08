from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String, Date, Float
import os
import datetime

#https://www.blog.pythonlibrary.org/2010/02/03/another-step-by-step-sqlalchemy-tutorial-part-1-of-2/

basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///'+os.path.join(basedir,"currfxdb.db"),echo=True)

metadata = MetaData(bind=engine)

fx_table = Table('currfxtbl', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('base', String(3)),
                    Column('foreign', String(3)),
                    Column('fxrate', Float),
                    Column('date', Date)
                    )

# create tables in database (unlock this to create a db)

ins = fx_table.insert()
result = engine.execute(ins, base="AUD", foreign="USD", fxrate=1.2345, date = datetime.date.today())
