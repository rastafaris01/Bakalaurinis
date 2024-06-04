import pandas as pd
from pandas import DataFrame

from sqlalchemy import create_engine
from constants.constant_url import URL

class AutoDB:
    def __init__(self):
        self.engine = create_engine(URL)
        self.data_file = 'constants/auto_data.csv'
        self.data = pd.read_csv(self.data_file)

    def load_data(self):
        df = pd.read_csv(self.data_file)
        df.drop_duplicates(inplace=True)
        df.rename(columns={
            'Power(BHP)': 'Power_BHP',
            'Torque(Nm)': 'Torque_Nm',
            'Fuel_Tank_Capacity(L)': 'Fuel_Tank_Capacity',
            'Mileage(kmpl)': 'Mileage_kmpl'
        }, inplace=True)

        transmission = df[['Transmission', 'Transmission_Type']].drop_duplicates()
        transmission.to_sql(name='transmission', con=self.engine, if_exists='replace', index_label='Transmission_id')

        engine_data = df[['Engine_Type', 'CC_Displacement', 'Power_BHP', 'Torque_Nm', 'Fuel_Type']].drop_duplicates()
        engine_data.to_sql(name='engines', con=self.engine, if_exists='replace', index_label='Engine_id')

        model_type_data = df[['Make', 'Body_Type', 'Seating_Capacity', 'Fuel_Tank_Capacity']].drop_duplicates()
        model_type_data.to_sql(name='model_type', con=self.engine, if_exists='replace', index_label='Model_type_id')

        model = df[['Car_Name', 'Mileage_kmpl', 'Model']].drop_duplicates()
        model.to_sql(name='model', con=self.engine, if_exists='replace', index_label='Model_id')

        market = df[['Price', 'Make_Year', 'Color', 'Mileage_Run', 'No_of_Owners']].drop_duplicates()
        market.to_sql(name='market', con=self.engine, if_exists='replace', index_label='Market_id')
