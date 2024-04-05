# SQL_Alchemy-Challenge
Climate Analysis API
Overview
This project provides a climate analysis API built with Flask, serving data from a SQLite database. The database includes historical precipitation and temperature data for Honolulu, Hawaii. This API is designed to support climate research and vacation planning by providing easy access to weather trends.

Features
Retrieve the last 12 months of precipitation data.
List all weather observation stations.
Fetch the temperature observations of the most active station for the last year.
Calculate the minimum, average, and maximum temperatures for a given date range.
Getting Started
Prerequisites
Python 3.7+
Flask
SQLAlchemy
numpy
Installation
Clone the repository to your local machine.
git clone https://github.com/yourusername/climate-analysis-api.git
Navigate to the project directory.
cd climate-analysis-api
Install the required Python packages.
pip install -r requirements.txt
Running the Application
Start the Flask development server.
python app.py
Access the API through http://127.0.0.1:5000/ in your web browser or API client.
API Endpoints
GET /: Home page listing all available routes.
GET /api/v1.0/precipitation: Returns JSON representation of the last 12 months of precipitation data.
GET /api/v1.0/stations: Returns a JSON list of stations.
GET /api/v1.0/tobs: Returns JSON list of temperature observations for the most active station over the last year.
GET /api/v1.0/<start> and GET /api/v1.0/<start>/<end>: Return a JSON list of the minimum, average, and maximum temperatures for a specified start or start-end range.
Examples
Retrieve precipitation data:
http://127.0.0.1:5000/api/v1.0/precipitation
Fetch temperature observations for the most active station:
http://127.0.0.1:5000/api/v1.0/tobs

