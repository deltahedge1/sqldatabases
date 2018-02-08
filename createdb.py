from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String, Date, Float
import os
import datetime

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
