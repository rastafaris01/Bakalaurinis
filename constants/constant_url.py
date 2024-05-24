import os


db_directory = os.path.abspath('C:/Users/admin/Documents/Fast track/visual studio code/Python/.venv/Bakalaurinis/database')
os.makedirs(db_directory, exist_ok=True)

URL = f'sqlite:///{os.path.join(db_directory, "Cars.db")}'
