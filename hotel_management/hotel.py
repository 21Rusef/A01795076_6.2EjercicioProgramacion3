'''
Clase de hotel:
-Creacion.
-Eliminacion.
-Modificacion.
-Mostrar detalles.
'''

import json
from database import Database


class Hotel:
    """
    Clase que representa un hotel con su información y manejo de reservas.
    """
    DB_FILE = "hotels.json"

    def __init__(self, hotel_id: int, name: str, location: str, rooms: int):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms = rooms
        self.reservations = []

    def to_dict(self):
        """Convierte la instancia a diccionario para almacenamiento."""
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "rooms": self.rooms,
            "reservations": self.reservations
        }

    @classmethod  # <-- Para modificar la clase de hotel simplemente.
    def create_hotel(cls, hotel_id, name, location, rooms):
        """Crea y almacena un hotel."""
        try:
            hotel = cls(hotel_id, name, location, rooms)
            Database.save(cls.DB_FILE, hotel.to_dict())
        except ValueError:  # pylint pidió ser más robusto en la excepción.
            print("Error: Valor inválido al crear el hotel.")
        except FileNotFoundError:
            print("Error: Archivo de base de datos no encontrado.")
        except PermissionError:
            print("Error: No tienes permisos para modificar el archivo.")

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Elimina un hotel del sistema."""
        Database.delete(cls.DB_FILE, "hotel_id", hotel_id)

    @classmethod
    def display_hotel(cls, hotel_id):
        """Muestra la información de un hotel."""
        hotel = Database.get(cls.DB_FILE, "hotel_id", hotel_id)
        if hotel:
            print(json.dumps(hotel, indent=4))
        else:
            print(f"Hotel {hotel_id} no encontrado.\n")

    @classmethod
    def modify_hotel(cls, hotel_id, name=None, location=None, rooms=None):
        """Modifica la información de un hotel."""
        hotel = Database.get(cls.DB_FILE, "hotel_id", hotel_id)
        if hotel:
            if name:
                hotel["name"] = name
            if location:
                hotel["location"] = location
            if rooms:
                hotel["rooms"] = rooms
            Database.update(cls.DB_FILE, "hotel_id", hotel_id, hotel)

    @classmethod
    def reserve_room(cls, hotel_id, customer_id):
        """Reserva una habitación si hay disponibilidad."""
        hotel = Database.get(cls.DB_FILE, "hotel_id", hotel_id)
        if hotel and hotel["rooms"] > 0:
            hotel["reservations"].append(customer_id)
            hotel["rooms"] -= 1
            Database.update(cls.DB_FILE, "hotel_id", hotel_id, hotel)
        else:
            print("No hay habitaciones disponibles.")

    @classmethod
    def cancel_reservation(cls, hotel_id, customer_id):
        """Cancela una reserva existente."""
        hotel = Database.get(cls.DB_FILE, "hotel_id", hotel_id)
        if hotel and customer_id in hotel["reservations"]:
            hotel["reservations"].remove(customer_id)
            hotel["rooms"] += 1
            Database.update(cls.DB_FILE, "hotel_id", hotel_id, hotel)
            print(f"Reserva cancelada para el cliente {customer_id}.")
