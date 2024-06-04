from db_modules.db_tables import create_tables
from db_modules.db_management import AutoDB
from routes import app


create_tables()

auto_db = AutoDB()
auto_db.load_data()


if __name__ == "__main__":
    app.run(debug=True)
