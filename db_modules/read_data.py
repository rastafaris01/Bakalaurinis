import pandas as pd
from sqlalchemy import create_engine
from constants.constant_url import URL

data_file = '../constants/auto_data.csv'
df = pd.read_csv('../constants/auto_data.csv')
engine = create_engine(URL)

transmission = df[['Transmission', 'Transmission_Type']].drop_duplicates()
# transmission.reset_index(drop=True, inplace=True)
# transmission.index.name = 'transmission_id'
transmission.to_sql(name='transmission', con=engine, if_exists='replace', index_label='transmission_id')

engine_data = df[['Engine_Type', 'CC_Displacement', 'Power(BHP)', 'Torque(Nm)', 'Fuel_Type']].drop_duplicates()
engine_data.to_sql(name='engine', con=engine, if_exists='replace', index_label='engine_id')

model_type = df[['Make', 'Body_Type', 'Seating_Capacity', 'Fuel_Tank_Capacity(L)']].drop_duplicates()
model_type.to_sql(name='model_type', con=engine, if_exists='replace', index_label='model_type_id')

model = df[['Car_Name', 'Mileage(kmpl)', 'Model', ]].drop_duplicates()
model.to_sql(name='model', con=engine, if_exists='replace', index_label='model_id')

market = df[['Price', 'Make_Year', 'Color', 'Mileage_Run', 'No_of_Owners']].drop_duplicates()
market.to_sql(name='market', con=engine, if_exists='replace', index_label='market_id')
# print(df.info())
# print(transmission)