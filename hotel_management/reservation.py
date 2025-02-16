'''
Módulo para el manejo de reservaciones con relación al hotel y el cliente.
'''

from database import Database
from hotel import Hotel


class Reservation:
    """Clase que gestiona las reservas de los hoteles por clientes."""

    DB_FILE = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        '''Convierte la data en diccionario.'''
        return {
            "reservation_id": self.reservation_id,
            "customer_id": self.customer_id,
            "hotel_id": self.hotel_id
        }

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Crea una nueva reserva."""
        Hotel.reserve_room(hotel_id, customer_id)
        reservation = cls(reservation_id, customer_id, hotel_id)
        Database.save(cls.DB_FILE, reservation.to_dict())

    @classmethod
    def cancel_reservation(cls, reservation_id):
        """Cancela una reserva."""
        reservation = Database.get(
            cls.DB_FILE,
            "reservation_id",
            reservation_id
            )
        if reservation:
            Hotel.cancel_reservation(
                reservation["hotel_id"],
                reservation["customer_id"]
                )
            Database.delete(cls.DB_FILE, "reservation_id", reservation_id)
