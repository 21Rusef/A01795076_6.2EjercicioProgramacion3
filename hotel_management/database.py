'''
Modulo para manejo de datos en json.
'''

import json
import os


class Database:
    """Clase para manejar almacenamiento en archivos JSON."""

    @staticmethod
    def _load_data(file):
        """Carga los datos desde un archivo JSON."""
        if not os.path.exists(file):
            return []
        try:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: El archivo {file} contiene datos inválidos.\n")
            return []

    @staticmethod
    def _save_data(file, data):
        """Guarda datos en un archivo JSON."""
        try:
            with open(file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {file}. Verifica la ruta")
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en {file}")
        except TypeError:
            print(f"Error: Tipo de dato no serializable al escribir en {file}")
        except json.JSONDecodeError:
            print(f"Error: El archivo {file} tiene datos JSON corruptos")

    @staticmethod
    def save(file, new_data):
        """Guarda un nuevo objeto en el archivo JSON."""
        data = Database._load_data(file)

        # Validar duplicados usando ID
        if any(item.get("id") == new_data.get("id") for item in data):
            print(
                f"El objeto {new_data.get('name')} ya existe en {file}.\n"
                )
            return

        data.append(new_data)
        Database._save_data(file, data)

    @staticmethod
    def get(file, key, value):
        """Obtiene un objeto específico desde un archivo JSON."""
        data = Database._load_data(file)
        return next((item for item in data if item.get(key) == value), None)

    @staticmethod
    def update(file, key, value, new_data):
        """Actualiza un objeto en el archivo JSON."""
        data = Database._load_data(file)
        updated = False

        for i, item in enumerate(data):
            if item.get(key) == value:
                data[i] = new_data
                updated = True
                break

        if updated:
            print("Registro actualizado.\n")
            Database._save_data(file, data)
        else:
            print(f"No se encontró el objeto con {key} = {value} en {file}.\n")

    @staticmethod
    def delete(file, key, value):
        """Elimina un objeto del archivo JSON."""
        data = Database._load_data(file)
        new_data = [item for item in data if item.get(key) != value]

        if len(new_data) < len(data):
            Database._save_data(file, new_data)
            print(f"Objeto con {key} = {value} eliminado de {file}.\n")
        else:
            print(f"No se encontró el objeto con {key} = {value} en {file}.\n")
