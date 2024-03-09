# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app=Flask(__name__)

@app.route("/")
def Welcome():
    return(f"<h1><center><strong>Welcome to SQLalchemy</h1></center></strong></br>"
           f"<center>/api/v1.0/precipitation</center></br>"
           f"<center>/api/v1.0/stations</center></br>"
           f"<center>/api/v1.0/tobs</center></br>"
           f"<center>/api/v1.0/temp/start</center></br>"
           f"<center>/api/v1.0/temp/start/end</center></br>")

@app.route("/api/v1.0/precipitation")
def Precip():
    previous_year = dt.date(2017,8,23)-dt.timedelta(days=365)
    result = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previous_year).all()
    session.close()
    precipitation = []
    for date, prcp in result:
        results = {}
        results["date"] = date 
        results["prcp"] = prcp
        precipitation.append(results)
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def Stations():
    result = session.query(Station.station).all()
    session.close()
    results = list(np.ravel(result))
    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():
    previous_year = dt.date(2017,8,23)-dt.timedelta(days=365)
    sel = [Measurement.date, Measurement.tobs]
    station_temps = session.query(*sel).\
            filter(Measurement.date >= previous_year, Measurement.station == 'USC00519281').all()
    session.close()
    observation_dates = []
    temperature_observations = []
    for date, observation in station_temps:
        observation_dates.append(date)
        temperature_observations.append(observation)
    result = dict(zip(observation_dates, temperature_observations))
    results = list(np.ravel(result))
    return jsonify(results)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def Temp(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        result = session.query(*sel).filter(Measurement.date >= start).all()
        session.close()
        results = list(np.ravel(result))
        return jsonify(results)
    result = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    results = list(np.ravel(result))
    return jsonify(results)

#################################################
# Flask Routes
#################################################
if __name__ == "__main__":
    app.run()