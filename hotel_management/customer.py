'''
Clase para manejo de clientes:
-Creacion.
-Modificacion.
-Eliminacion.
-Mostrar detalles.
'''

from database import Database


class Customer:
    """Clase que representa un cliente."""

    DB_FILE = "customers.json"

    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        '''Convierte data a diccionario para json.'''
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Crea un nuevo cliente."""
        customer = cls(customer_id, name, email)
        Database.save(cls.DB_FILE, customer.to_dict())

    @classmethod
    def delete_customer(cls, customer_id):
        """Elimina un cliente."""
        Database.delete(cls.DB_FILE, "customer_id", customer_id)

    @classmethod
    def display_customer(cls, customer_id):
        """Muestra la información de un cliente."""
        customer = Database.get(cls.DB_FILE, "customer_id", customer_id)
        if customer:
            print(customer)
        else:
            print(f"Cliente {customer_id} no encontrado.")

    @classmethod
    def modify_customer(cls, customer_id, name=None, email=None):
        """Modifica la información de un cliente en la base de datos."""
        customer = Database.get(cls.DB_FILE, "customer_id", customer_id)
        if customer:
            if name:
                customer["name"] = name
            if email:
                customer["email"] = email

            # Actualizamos archivo JSON.
            Database.update(cls.DB_FILE, "customer_id", customer_id, customer)
        else:
            print(f"⚠ Error: Cliente con ID {customer_id} no encontrado.")
