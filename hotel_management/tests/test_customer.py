'''
Módulo para hacer pruebas a la clase de clientes con ejemplos de cada función.
'''

import unittest
import os
import json
from customer import Customer
from database import Database


class TestCustomer(unittest.TestCase):
    """Pruebas unitarias para la clase Customer."""

    DB_FILE = "customers_test.json"

    print("Pruebas para clase cliente.")

    def setUp(self):
        """Prepara el entorno antes de cada prueba."""
        if os.path.exists(self.DB_FILE):
            os.remove(self.DB_FILE)
        with open(self.DB_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    def test_create_customer(self):
        """Prueba la creación de un cliente."""
        Customer.DB_FILE = self.DB_FILE  # Usamos base de datos de prueba
        Customer.create_customer(1, "John Doe", "john@example.com")
        customer = Database.get(self.DB_FILE, "customer_id", 1)
        self.assertIsNotNone(customer)
        self.assertEqual(customer["name"], "John Doe")
        self.assertEqual(customer["email"], "john@example.com")

    def test_delete_customer(self):
        """Prueba la eliminación de un cliente."""
        Customer.DB_FILE = self.DB_FILE
        Customer.create_customer(2, "Jane Doe", "jane@example.com")
        Customer.delete_customer(2)
        customer = Database.get(self.DB_FILE, "customer_id", 2)
        self.assertIsNone(customer)

    def test_display_customer(self):
        """Prueba la visualización de información de un cliente."""
        Customer.DB_FILE = self.DB_FILE
        Customer.create_customer(3, "Alice", "alice@example.com")
        with open(self.DB_FILE, "r", encoding="utf-8") as f:
            customers = json.load(f)
        self.assertEqual(customers[0]["name"], "Alice")

    def tearDown(self):
        """Elimina el archivo de prueba después de cada prueba."""
        if os.path.exists(self.DB_FILE):
            os.remove(self.DB_FILE)


if __name__ == "__main__":
    unittest.main()
