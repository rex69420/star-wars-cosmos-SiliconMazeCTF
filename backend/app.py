from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

SWAPI_BASE_URL = "https://swapi.dev/api/"

def fetch_planet_data():
    response = requests.get(f"{SWAPI_BASE_URL}planets/")
    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    return []

@app.route('/api/planets')
def get_planets():
    planets = fetch_planet_data()
    return jsonify(planets)

if __name__ == '__main__':
    app.run(debug=True)
