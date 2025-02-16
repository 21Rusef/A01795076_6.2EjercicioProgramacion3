'''
Sistema para Hotel con:
-Administracion de hotel.
-Administracion de clientes.
-Administracion de reservas.
'''

from hotel import Hotel
from customer import Customer
from reservation import Reservation


def manage_hotels():
    """Gestión de hoteles en el sistema."""
    print("\n--- GESTIÓN DE HOTELES ---")
    print("1. Crear Hotel")
    print("2. Eliminar Hotel")
    print("3. Mostrar Información de un Hotel")
    print("4. Modificar Hotel")
    print("5. Reservar Habitación")
    print("6. Cancelar Reserva")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hotel_id = int(input("ID del hotel: "))
        name = input("Nombre del hotel: ")
        location = input("Ubicación: ")
        rooms = int(input("Número de habitaciones: "))
        Hotel.create_hotel(hotel_id, name, location, rooms)
        print("\nHotel creado.")

    elif opcion == "2":
        hotel_id = int(input("ID del hotel a eliminar: "))
        Hotel.delete_hotel(hotel_id)
        print("\nHotel eliminado.")

    elif opcion == "3":
        hotel_id = int(input("ID del hotel a mostrar: "))
        Hotel.display_hotel(hotel_id)

    elif opcion == "4":
        print("Deja en blanco para no modificar")
        hotel_id = int(input("ID del hotel a modificar: "))
        name = input("Nuevo nombre: ")
        location = input("Nueva ubicación: ")
        rooms = input("Nuevo número de habitaciones: ")
        Hotel.modify_hotel(
            hotel_id,
            name or None,
            location or None,
            int(rooms) if rooms else None
            )
        print("\nHotel modificado.")

    elif opcion == "5":
        hotel_id = int(input("ID del hotel: "))
        customer_id = int(input("ID del cliente: "))
        Hotel.reserve_room(hotel_id, customer_id)
        print("\nReservacion creada.")

    elif opcion == "6":
        hotel_id = int(input("ID del hotel: "))
        customer_id = int(input("ID del cliente: "))
        Hotel.cancel_reservation(hotel_id, customer_id)
        print("\nReservacion cancelada.")


def manage_customers():
    """Gestión de clientes en el sistema."""
    print("\n--- GESTIÓN DE CLIENTES ---")
    print("7. Crear Cliente")
    print("8. Eliminar Cliente")
    print("9. Mostrar Información de Cliente")
    print("10. Modificar Cliente")

    opcion = input("Seleccione una opción: ")

    if opcion == "7":
        customer_id = int(input("ID del cliente: "))
        name = input("Nombre del cliente: ")
        email = input("Email: ")
        Customer.create_customer(customer_id, name, email)
        print("\nCliente creado.")

    elif opcion == "8":
        customer_id = int(input("ID del cliente a eliminar: "))
        Customer.delete_customer(customer_id)
        print("\nCliente eliminado.")

    elif opcion == "9":
        customer_id = int(input("ID del cliente a mostrar: "))
        Customer.display_customer(customer_id)

    elif opcion == "10":
        print("Deja en blanco para no modificar")
        customer_id = int(input("ID del cliente a modificar: "))
        name = input("Nuevo nombre: ")
        email = input("Nuevo email: ")
        Customer.modify_customer(customer_id, name or None, email or None)
        print("\nCliente modificado.")


def manage_reservations():
    """Gestión de reservas en el sistema."""
    print("\n--- GESTIÓN DE RESERVAS ---")
    print("11. Crear Reserva")
    print("12. Cancelar Reserva")

    opcion = input("Seleccione una opción: ")

    if opcion == "11":
        reservation_id = int(input("ID de la reserva: "))
        customer_id = int(input("ID del cliente: "))
        hotel_id = int(input("ID del hotel: "))
        Reservation.create_reservation(reservation_id, customer_id, hotel_id)
        print("\nReservacion creada.")

    elif opcion == "12":
        reservation_id = int(input("ID de la reserva a cancelar: "))
        Reservation.cancel_reservation(reservation_id)
        print("\nReservacion cancelada.")


def main():
    """Menú principal del sistema de gestión de hoteles."""
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE HOTELES ---")
        print("1-6: Gestión de Hoteles")
        print("7-10: Gestión de Clientes")
        print("11-12: Gestión de Reservas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2", "3", "4", "5", "6"]:
            manage_hotels()
        elif opcion in ["7", "8", "9", "10"]:
            manage_customers()
        elif opcion in ["11", "12"]:
            manage_reservations()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
