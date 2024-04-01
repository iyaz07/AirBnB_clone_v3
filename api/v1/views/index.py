#!/usr/bin/python3
"""Defines the routes and handlers for the API endpoints"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def Stats():
    """Get Stats"""
    return_dict = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City')
        'places': storage.count('place')
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User');
        }
    return jsonify(return_dict)
