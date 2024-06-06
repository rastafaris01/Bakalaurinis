from db_modules.db_tables import create_tables, ManageCars
from db_modules.db_management import AutoDB
from routes import app




if __name__ == "__main__":
    create_tables()
    auto_db = AutoDB()
    auto_db.load_data()

    app.run(debug=True)
