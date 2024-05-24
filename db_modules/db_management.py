import pandas as pd
from sqlalchemy import create_engine
from constants.constant_url import URL

engine = create_engine(URL)

# data_file = '../constants/auto_data.csv'
# df = pd.read_csv('../constants/auto_data.csv')
'''
CRUD
'''

class AutoDB:
    def __init__(self):
        self.engine = create_engine(URL)
        self.data_file = '../constants/auto_data.csv'

    def load_data(self):
        df = pd.read_csv(self.data_file)

        df.rename(columns={
            'Power(BHP)': 'Power_BHP',
            'Torque(Nm)': 'Torque_Nm',
            'Fuel_Tank_Capacity(L)': 'Fuel_Tank_Capacity',
            'Mileage(kmpl)': 'Mileage_kmpl'
        }, inplace=True)

        # transmission = df[['Transmission', 'Transmission_Type']].drop_duplicates()
        # transmission.to_sql(name='transmission', con=self.engine, if_exists='replace', index_label='transmission_id')
        #
        # engine_data = df[['Engine_Type', 'CC_Displacement', 'Power_BHP', 'Torque_Nm', 'Fuel_Type']].drop_duplicates()
        # engine_data.to_sql(name='engine', con=self.engine, if_exists='replace', index_label='engine_id')
        #
        # model_type_data = df[['Make', 'Body_Type', 'Seating_Capacity', 'Fuel_Tank_Capacity']].drop_duplicates()
        # model_type_data.to_sql(name='model_type', con=self.engine, if_exists='replace', index_label='model_type_id')
        #
        # model = df[['Car_Name', 'Mileage_kmpl', 'Model']].drop_duplicates()
        # model.to_sql(name='model', con=self.engine, if_exists='replace', index_label='model_id')
        #
        # market = df[['Price', 'Make_Year', 'Color', 'Mileage_Run', 'No_of_Owners']].drop_duplicates()
        # market.to_sql(name='market', con=self.engine, if_exists='replace', index_label='market_id')
        #

auto_db = AutoDB()
auto_db.load_data()


