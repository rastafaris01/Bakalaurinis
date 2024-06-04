from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from constants.constant_url import URL

Base = declarative_base()


class Transmission(Base):
    __tablename__ = 'transmission'
    Transmission_id = Column(Integer, primary_key=True, autoincrement=True)
    Transmission = Column(String, nullable=False)
    Transmission_Type = Column(String, nullable=False)
    models = relationship('Model', back_populates='Transmission')


class Engine(Base):
    __tablename__ = 'engines'
    Engine_id = Column(Integer, primary_key=True, autoincrement=True)
    Engine_Type = Column(String, nullable=False)
    CC_Displacement = Column(Float, nullable=False)
    Power_BHP = Column(Float, nullable=False)
    Torque_Nm = Column(Float, nullable=False)
    Fuel_Type = Column(String, nullable=False)
    models = relationship('Model', back_populates='Engine')


class ModelTypes(Base):
    __tablename__ = 'model_type'
    Model_type_id = Column(Integer, primary_key=True, autoincrement=True)
    Make = Column(String, nullable=False)
    Body_Type = Column(String, nullable=False)
    Seating_Capacity = Column(Integer, nullable=False)
    Fuel_Tank_Capacity = Column(Float, nullable=False)
    models = relationship('Model', back_populates='Model_type')


class Model(Base):
    __tablename__ = "model"
    Model_id = Column(Integer, primary_key=True, autoincrement=True)
    Car_Name = Column(String, nullable=False)
    Mileage_kmpl = Column(Float, nullable=False)
    Model = Column(String, nullable=False)
    Transmission_id = Column(Integer, ForeignKey('transmission.Transmission_id'))
    Engine_id = Column(Integer, ForeignKey('engines.Engine_id'))
    Model_type_id = Column(Integer, ForeignKey('model_type.Model_type_id'))

    Transmission = relationship('Transmission', back_populates='models')
    Engine = relationship('Engine', back_populates='models')
    Model_type = relationship('ModelTypes', back_populates='models')
    markets = relationship('Market', back_populates='model')


class Market(Base):
    __tablename__ = "market"
    Market_id = Column(Integer, primary_key=True, autoincrement=True)
    Price = Column(Float, nullable=False)
    Make_Year = Column(Integer, nullable=False)
    Color = Column(String, nullable=False)
    Mileage_Run = Column(Float, nullable=False)
    No_of_Owners = Column(Integer, nullable=False)
    Model_id = Column(Integer, ForeignKey('model.Model_id'))

    model = relationship('Model', back_populates='markets')



engine = create_engine(URL)
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)
