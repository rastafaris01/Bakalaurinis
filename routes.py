from typing import List, Type

from flask import Flask, render_template

from db_modules.db_tables import session, Transmission, Engine, Model, ModelTypes, Market

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
