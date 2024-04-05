from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import numpy as np
import datetime as dt

app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine(r"sqlite:///C:\Users\Tasnia Wahid\Desktop\sqlalchemy\Starter_Code\Resources\hawaii.sqlite")
# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all available API routes."""
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    # Calculate the date 1 year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query all precipitation data from the last year
    results = session.query(Measurement.date, Measurement.prcp).\
              filter(Measurement.date >= one_year_ago).all()
    session.close()

    # Convert query results to a dictionary using date as the key and prcp as the value
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Query all stations
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    stations_list = list(np.ravel(results))

    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    # Calculate the date 1 year ago from the last data point in the database
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # Query the dates and temperature observations of the most active station for the last year of data
    results = session.query(Measurement.tobs).\
              filter(Measurement.station == 'USC00519281').\
              filter(Measurement.date >= one_year_ago).all()
    session.close()

    # Convert list of tuples into normal list
    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end=None):
    session = Session(engine)
    # Construct the query based on whether an end date is provided
    if end:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    else:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).all()
    session.close()

    # Convert list of tuples into normal list
    temps = list(np.ravel(results))

    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)
