#!/usr/bin/python
import unittest
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestNewClasses(unittest.TestCase):
    """Test cases for new classes."""

    def test_state(self):
        """Test State class."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")
        self.assertIsInstance(state, State)

    def test_city(self):
        """Test City class."""
        city = City()
        city.state_id = "state_id"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "state_id")
        self.assertEqual(city.name, "San Francisco")
        self.assertIsInstance(city, City)

    def test_amenity(self):
        """Test Amenity class."""
        amenity = Amenity()
        amenity.name = "Wi-Fi"
        self.assertEqual(amenity.name, "Wi-Fi")
        self.assertIsInstance(amenity, Amenity)

    def test_place(self):
        """Test Place class."""
        place = Place()
        place.city_id = "city_id"
        place.user_id = "user_id"
        place.name = "Luxury Villa"
        place.description = "A beautiful villa by the beach."
        place.number_rooms = 5
        place.number_bathrooms = 3
        place.max_guest = 10
        place.price_by_night = 500
        place.latitude = 37.7749
        place.longitude = -122.4194
        self.assertEqual(place.city_id, "city_id")
        self.assertEqual(place.user_id, "user_id")
        self.assertEqual(place.name, "Luxury Villa")
        self.assertEqual(place.description, "A beautiful villa by the beach.")
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 3)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 500)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertIsInstance(place, Place)

    def test_review(self):
        """Test Review class."""
        review = Review()
        review.place_id = "place_id"
        review.user_id = "user_id"
        review.text = "Amazing place! Highly recommend."
        self.assertEqual(review.place_id, "place_id")
        self.assertEqual(review.user_id, "user_id")
        self.assertEqual(review.text, "Amazing place! Highly recommend.")
        self.assertIsInstance(review, Review)

if __name__ == "__main__":
    unittest.main()