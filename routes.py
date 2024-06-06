from flask import Flask, render_template, request, redirect, url_for
from db_modules import create_tables, session, Transmission, Engine, Model, ModelTypes, Market, ManageCars

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/transmissions")
def transmissions():
    transmissions = session.query(Transmission).all()
    return render_template("transmissions.html", transmissions=transmissions)


@app.route("/engines")
def engines():
    engines = session.query(Engine).all()
    return render_template("engines.html", engines=engines)


@app.route('/models')
def models():
    models = session.query(Model).all()
    return render_template("models.html", models=models)


@app.route('/model_types')
def model_types():
    model_types = session.query(ModelTypes).all()
    return render_template('model_types.html', model_types=model_types)


@app.route('/markets')
def markets():
    markets = session.query(Market).all()
    return render_template('markets.html', markets=markets)


@app.route("/cars")
def cars():
    transmissions = session.query(Transmission).all()
    engines = session.query(Engine).all()
    model_types = session.query(ModelTypes).all()
    models = session.query(Model).all()
    markets = session.query(Market).all()
    return render_template("cars.html", transmissions=transmissions, engines=engines,
                           model_types=model_types, models=models, markets=markets)


@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        car_name = request.form['car_name']
        mileage_kmpl = request.form['mileage_kmpl']
        model = request.form['model']
        transmission = request.form['transmission']
        transmission_type = request.form['transmission_type']
        engine_type = request.form['engine_type']
        cc_displacement = request.form['cc_displacement']
        power_bhp = request.form['power_bhp']
        torque_nm = request.form['torque_nm']
        fuel_type = request.form['fuel_type']
        make = request.form['make']
        body_type = request.form['body_type']
        seating_capacity = request.form['seating_capacity']
        fuel_tank_capacity = request.form['fuel_tank_capacity']
        price = request.form['price']
        make_year = request.form['make_year']
        color = request.form['color']
        mileage_run = request.form['mileage_run']
        no_of_owners = request.form['no_of_owners']

        manage_cars = ManageCars(session)
        manage_cars.add_car(car_name, mileage_kmpl, model, transmission,
                    transmission_type, engine_type, cc_displacement,
                    power_bhp, torque_nm, fuel_type, make, body_type,
                    seating_capacity, fuel_tank_capacity, price, make_year,
                    color, mileage_run, no_of_owners)

        return redirect(url_for('home'))

    return render_template('add_car.html')


if __name__ == "__main__":
    create_tables()
    app.run(debug=True)
