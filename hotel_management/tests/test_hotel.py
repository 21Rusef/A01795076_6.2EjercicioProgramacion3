'''
Módulo para hacer pruebas a la clase de hotel con ejemplos de cada función.
'''

import unittest
import os
import json
from hotel import Hotel
from database import Database


class TestHotel(unittest.TestCase):
    """Pruebas unitarias para la clase Hotel."""

    DB_FILE = "hotels_test.json"

    print("-- Pruebas para clase Hotel. --")

    def setUp(self):
        """Prepara el entorno antes de cada prueba."""
        if os.path.exists(self.DB_FILE):
            os.remove(self.DB_FILE)
        with open(self.DB_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    def test_create_hotel(self):
        """Prueba la creación de un hotel."""
        Hotel.DB_FILE = self.DB_FILE  # Usamos base de datos de prueba
        Hotel.create_hotel(1, "Hotel Tec", "Mty", 100)
        hotel = Database.get(self.DB_FILE, "hotel_id", 1)
        self.assertIsNotNone(hotel)
        self.assertEqual(hotel["name"], "Hotel Tec")
        self.assertEqual(hotel["location"], "Mty")
        self.assertEqual(hotel["rooms"], 100)

    def test_delete_hotel(self):
        """Prueba la eliminación de un hotel."""
        Hotel.DB_FILE = self.DB_FILE
        Hotel.create_hotel(2, "Hotel ABC", "Leon", 15)
        Hotel.delete_hotel(2)
        hotel = Database.get(self.DB_FILE, "hotel_id", 2)
        self.assertIsNone(hotel)

    def test_modify_hotel(self):
        """Prueba la modificación de un hotel."""
        Hotel.DB_FILE = self.DB_FILE
        Hotel.create_hotel(
            3,
            "Hotel Fiesta",
            "Ags",
            200
            )
        Hotel.modify_hotel(
            3,
            name="Hotel Nuevo",
            location="CDMX",
            rooms=25
            )
        hotel = Database.get(self.DB_FILE, "hotel_id", 3)
        self.assertEqual(hotel["name"], "Hotel Nuevo")
        self.assertEqual(hotel["location"], "CDMX")
        self.assertEqual(hotel["rooms"], 25)

    def test_reserve_room(self):
        """Prueba la reserva de una habitación en un hotel."""
        Hotel.DB_FILE = self.DB_FILE
        Hotel.create_hotel(4, "Hotel Reserva", "Ciudad R", 5)
        Hotel.reserve_room(4, 101)  # Cliente 101
        hotel = Database.get(self.DB_FILE, "hotel_id", 4)
        self.assertEqual(hotel["rooms"], 4)  # Se redujo una habitación
        self.assertIn(101, hotel["reservations"])

    def test_cancel_reservation(self):
        """Prueba la cancelación de una reserva en un hotel."""
        Hotel.DB_FILE = self.DB_FILE
        Hotel.create_hotel(5, "Hotel Cancelación", "Ciudad C", 3)
        Hotel.reserve_room(5, 102)
        Hotel.cancel_reservation(5, 102)
        hotel = Database.get(self.DB_FILE, "hotel_id", 5)
        self.assertEqual(hotel["rooms"], 3)  # Se recuperó la habitación
        self.assertNotIn(102, hotel["reservations"])

    def tearDown(self):
        """Elimina el archivo de prueba después de cada prueba."""
        if os.path.exists(self.DB_FILE):
            os.remove(self.DB_FILE)


if __name__ == "__main__":
    unittest.main()
