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
    __tablename__ = 'engine'
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
    Engine_id = Column(Integer, ForeignKey('engine.Engine_id'))
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


class ManageCars:
    def __init__(self, session):
        self.session = session

    def add_car(self, car_name, mileage_kmpl, model, transmission,
                transmission_type, engine_type, cc_displacement,
                power_bhp, torque_nm, fuel_type, make, body_type,
                seating_capacity, fuel_tank_capacity, price, make_year,
                color, mileage_run, no_of_owners):

        new_transmission = Transmission(Transmission=transmission, Transmission_Type=transmission_type)
        self.session.add(new_transmission)

        new_engine = Engine(Engine_Type=engine_type, CC_Displacement=cc_displacement, Power_BHP=power_bhp,
                            Torque_Nm=torque_nm, Fuel_Type=fuel_type)
        self.session.add(new_engine)

        new_model_type = ModelTypes(Make=make, Body_Type=body_type,
                                    Seating_Capacity=seating_capacity, Fuel_Tank_Capacity=fuel_tank_capacity)
        self.session.add(new_model_type)

        new_model = Model(Car_Name=car_name, Mileage_kmpl=mileage_kmpl, Model=model)
        self.session.add(new_model)

        new_market = Market(Price=price, Make_Year=make_year, Color=color,
                            Mileage_Run=mileage_run, No_of_Owners=no_of_owners)
        self.session.add(new_market)

        self.session.commit()

        return {
            'Transmission': new_transmission,
            'Engine': new_engine,
            'ModelTypes': new_model_type,
            'Model': new_model,
            'Market': new_market
        }


engine = create_engine(URL)
Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    Base.metadata.create_all(engine)