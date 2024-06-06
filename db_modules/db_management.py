import pandas as pd
from sqlalchemy import create_engine
from db_modules.db_tables import Base
from constants.constant_url import URL
import os

class AutoDB:
    def __init__(self):
        self.engine = create_engine(URL)
        self.data_file = os.path.join(os.path.dirname(__file__), '..', 'constants', 'auto_data.csv')

    def load_data(self):
        df = pd.read_csv(self.data_file)
        df.drop_duplicates(inplace=True)
        df.rename(columns={
            'Power(BHP)': 'Power_BHP',
            'Torque(Nm)': 'Torque_Nm',
            'Fuel_Tank_Capacity(L)': 'Fuel_Tank_Capacity',
            'Mileage(kmpl)': 'Mileage_kmpl'
        }, inplace=True)

        transmission_df = df[['Transmission', 'Transmission_Type']].drop_duplicates().reset_index(drop=True)
        transmission_df.index += 1
        transmission_df.index.name = 'Transmission_id'

        transmission_df.to_sql(name='transmission', con=self.engine, if_exists='replace', index=True)


        engine_df = df[
            ['Engine_Type', 'CC_Displacement', 'Power_BHP', 'Torque_Nm', 'Fuel_Type']].drop_duplicates().reset_index(
            drop=True)
        engine_df.index += 1
        engine_df.index.name = 'Engine_id'
        engine_df.to_sql(name='engine', con=self.engine, if_exists='replace', index=True)


        model_type_df = df[
            ['Make', 'Body_Type', 'Seating_Capacity', 'Fuel_Tank_Capacity']].drop_duplicates().reset_index(drop=True)
        model_type_df.index += 1
        model_type_df.index.name = 'Model_type_id'
        model_type_df.to_sql(name='model_type', con=self.engine, if_exists='replace', index=True)


        model_df = df[['Car_Name', 'Mileage_kmpl', 'Model', 'Transmission', 'Engine_Type', 'Make',
                       'Body_Type']].drop_duplicates().reset_index(drop=True)
        model_df = model_df.merge(transmission_df.reset_index()[['Transmission', 'Transmission_id']], on='Transmission',
                                  how='left').drop(columns=['Transmission'])
        model_df = model_df.merge(engine_df.reset_index()[['Engine_Type', 'Engine_id']], on='Engine_Type',
                                  how='left').drop(columns=['Engine_Type'])
        model_df = model_df.merge(model_type_df.reset_index()[['Make', 'Body_Type', 'Model_type_id']],
                                  on=['Make', 'Body_Type'], how='left').drop(columns=['Make', 'Body_Type'])
        model_df.index += 1
        model_df.index.name = 'Model_id'
        model_df.to_sql(name='model', con=self.engine, if_exists='replace', index=True)


        market_df = df[['Price', 'Make_Year', 'Color', 'Mileage_Run', 'No_of_Owners', 'Car_Name', 'Mileage_kmpl',
                        'Model']].drop_duplicates().reset_index(drop=True)
        market_df = market_df.merge(model_df.reset_index()[['Car_Name', 'Mileage_kmpl', 'Model', 'Model_id']],
                                    on=['Car_Name', 'Mileage_kmpl', 'Model'], how='left').drop(columns=['Car_Name', 'Mileage_kmpl','Model',])
        market_df.index += 1
        market_df.index.name = 'Market_id'
        market_df.to_sql(name='market', con=self.engine, if_exists='replace', index=True)

