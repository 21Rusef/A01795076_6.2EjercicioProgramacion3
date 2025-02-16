'''
Módulo para hacer pruebas a la clase de reservaciones
con ejemplos de cada función.
'''

import unittest
import os
import json
from reservation import Reservation
from hotel import Hotel
from customer import Customer
from database import Database


class TestReservation(unittest.TestCase):
    """Pruebas unitarias para la clase Reservation."""

    HOTEL_DB_FILE = "hotels_test.json"
    CUSTOMER_DB_FILE = "customers_test.json"
    RESERVATION_DB_FILE = "reservations_test.json"

    print("-- Pruebas para clase de reservaciones. --")

    def setUp(self):
        """Prepara el entorno antes de cada prueba."""
        for file in [
            self.HOTEL_DB_FILE,
            self.CUSTOMER_DB_FILE,
            self.RESERVATION_DB_FILE
        ]:
            if os.path.exists(file):
                os.remove(file)

            # Crea un archivo vacio.
            with open(file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def test_create_reservation(self):
        """Prueba la creación de una reserva."""
        Hotel.DB_FILE = self.HOTEL_DB_FILE
        Customer.DB_FILE = self.CUSTOMER_DB_FILE
        Reservation.DB_FILE = self.RESERVATION_DB_FILE

        # Crear hotel y cliente
        Hotel.create_hotel(10, "Hotel Prueba", "Ciudad P", 5)
        Customer.create_customer(201, "Carlos Pérez", "carlos@example.com")

        # Crear reserva
        Reservation.create_reservation(301, 201, 10)

        # Validar reserva
        reservation = Database.get(
            self.RESERVATION_DB_FILE,
            "reservation_id",
            301
            )
        self.assertIsNotNone(reservation)
        self.assertEqual(reservation["customer_id"], 201)
        self.assertEqual(reservation["hotel_id"], 10)

    def test_cancel_reservation(self):
        """Prueba la cancelación de una reserva."""
        Hotel.DB_FILE = self.HOTEL_DB_FILE
        Customer.DB_FILE = self.CUSTOMER_DB_FILE
        Reservation.DB_FILE = self.RESERVATION_DB_FILE

        # Crear hotel y cliente
        Hotel.create_hotel(11, "Hotel Ejemplo", "Ciudad E", 3)
        Customer.create_customer(202, "Ana Gómez", "ana@example.com")

        # Crear y cancelar reserva
        Reservation.create_reservation(302, 202, 11)
        Reservation.cancel_reservation(302)

        # Validar que la reserva se eliminó
        reservation = Database.get(
            self.RESERVATION_DB_FILE,
            "reservation_id",
            302
            )
        self.assertIsNone(reservation)

    def test_reservation_affects_hotel_availability(self):
        """Prueba que una reserva afecta la disponibilidad del hotel."""
        Hotel.DB_FILE = self.HOTEL_DB_FILE
        Customer.DB_FILE = self.CUSTOMER_DB_FILE
        Reservation.DB_FILE = self.RESERVATION_DB_FILE

        # Crear hotel con 2 habitaciones
        Hotel.create_hotel(12, "Hotel Habitaciones", "Ciudad H", 2)
        Customer.create_customer(203, "Luis Martínez", "luis@example.com")
        Customer.create_customer(204, "María Torres", "maria@example.com")

        # Reservar habitaciones
        Reservation.create_reservation(303, 203, 12)
        Reservation.create_reservation(304, 204, 12)

        # Validar que el hotel no tiene habitaciones disponibles
        hotel = Database.get(self.HOTEL_DB_FILE, "hotel_id", 12)
        self.assertEqual(hotel["rooms"], 0)

    def test_cancelling_reservation_frees_hotel_room(self):
        """
        Cancelar una reserva y se libera una habitación en el hotel.
        """
        Hotel.DB_FILE = self.HOTEL_DB_FILE
        Customer.DB_FILE = self.CUSTOMER_DB_FILE
        Reservation.DB_FILE = self.RESERVATION_DB_FILE

        # Crear hotel con 1 habitación
        Hotel.create_hotel(13, "Hotel Solo Uno", "Ciudad S", 1)
        Customer.create_customer(205, "Pedro Rojas", "pedro@example.com")

        # Hacer y cancelar reserva
        Reservation.create_reservation(305, 205, 13)
        Reservation.cancel_reservation(305)

        # Validar que la habitación vuelve a estar disponible
        hotel = Database.get(self.HOTEL_DB_FILE, "hotel_id", 13)
        self.assertEqual(hotel["rooms"], 1)

    def tearDown(self):
        """Elimina los archivos de prueba después de cada prueba."""
        for file in [
            self.HOTEL_DB_FILE,
            self.CUSTOMER_DB_FILE,
            self.RESERVATION_DB_FILE
        ]:
            if os.path.exists(file):
                os.remove(file)


if __name__ == "__main__":
    unittest.main()
