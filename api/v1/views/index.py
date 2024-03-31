#!/usr/bin/python3
"""Defines the routes and handlers for the API endpoints"""

from api.v1.views import app_views
from flask import jsonify


hbnbObjects = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnbStats():
    """hbnbStats"""
    return_dict = {}
    for key, value in hbnbObjects.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)


if __name__ == "__main__":
    pass
