import os
import csv

class FileManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_table(self, table_name, columns):
        table_file = os.path.join(self.db_path, f"{table_name}.csv")
        if not os.path.exists(table_file):
            with open(table_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(columns)
            print(f"La tabla '{table_name}' ha sido creada exitosamente.")
        else:
            print(f"La tabla '{table_name}' ya existe.")

    def insert(self, table_name, data):
        table_file = os.path.join(self.db_path, f"{table_name}.csv")
        if os.path.exists(table_file):
            with open(table_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            print("Datos insertados exitosamente.")
        else:
            print(f"La tabla '{table_name}' no existe.")

    def select_all(self, table_name):
        table_file = os.path.join(self.db_path, f"{table_name}.csv")
        if os.path.exists(table_file):
            with open(table_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        else:
            print(f"La tabla '{table_name}' no existe.")

    # Puedes implementar otras funcionalidades, como update, delete, etc., utilizando la misma lógica de manejo de archivos planos.

