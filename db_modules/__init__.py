from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from constants.constant_url import URL
from db_modules.db_tables import Transmission, Engine, ModelTypes, Model, Market
from flask import Flask
from db_modules.db_management import AutoDB
from db_modules.db_tables import create_tables

Base = declarative_base()

engine = create_engine(URL)

Session = sessionmaker(bind=engine)
session = Session()

auto_db = AutoDB()
auto_db.load_data()


create_tables()


app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
