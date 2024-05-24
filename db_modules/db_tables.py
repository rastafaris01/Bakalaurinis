from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from constants.constant_url import URL

Base = declarative_base()


class Transmission(Base):
    __tablename__ = 'transmission'
    transmission_id = Column(Integer, primary_key=True, autoincrement=True)
    Transmission = Column(String, nullable=False)
    Transmission_Type = Column(String, nullable=False)


class Engine(Base):
    __tablename__ = 'engine'
    engine_id = Column(Integer, primary_key=True, autoincrement=True)
    Engine_Type = Column(String, nullable=False)
    CC_Displacement = Column(Float, nullable=False)
    Power_BHP = Column(Float, nullable=False)
    Torque_Nm = Column(Float, nullable=False)
    Fuel_Type = Column(String, nullable=False)


class ModelTypes(Base):
    __tablename__ = 'model_type'
    model_type_id = Column(Integer, primary_key=True, autoincrement=True)
    Make = Column(String, nullable=False)
    Body_Type = Column(String, nullable=False)
    Seating_Capacity = Column(Integer, nullable=False)
    Fuel_Tank_Capacity = Column(Float, nullable=False)


class Model(Base):
    __tablename__ = "model"
    model_id = Column(Integer, primary_key=True, autoincrement=True)
    Car_Name = Column(String, nullable=False)
    Mileage_kmpl = Column(Float, nullable=False)
    Model = Column(String, nullable=False)


class Market(Base):
    __tablename__ = "market"
    market_id = Column(Integer, primary_key=True, autoincrement=True)
    Price = Column(Float, nullable=False)
    Make_Year = Column(Integer, nullable=False)
    Color = Column(String, nullable=False)
    Mileage_Run = Column(Float, nullable=False)
    No_of_Owners = Column(Integer, nullable=False)

engine = create_engine(URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

