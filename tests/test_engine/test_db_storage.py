#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.base_model import Base
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}

class TestDBStorage(unittest.TestCase):
    """Test the DBStorage class"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_get(self):
        """Test that get returns specific object, or none"""
        new_state = State(name="New York")
        new_state.save()
        new_user = User(email="bob@foobar.com", password="password")
        new_user.save()
        self.assertIs(new_state, models.storage.get("State", new_state.id))
        self.assertIs(None, models.storage.get("State", "blah"))
        self.assertIs(None, models.storage.get("blah", "blah"))
        self.assertIs(new_user, models.storage.get("User", new_user.id))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_count(self):
        """test that new adds an object to the database"""
        initial_count = models.storage.count()
        self.assertEqual(models.storage.count("Blah"), 0)
        new_state = State(name="Florida")
        new_state.save()
        new_user = User(email="bob@foobar.com", password="password")
        new_user.save()
        self.assertEqual(models.storage.count("State"), initial_count + 1)
        self.assertEqual(models.storage.count(), initial_count + 2)