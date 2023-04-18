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
            
    def get_table_names(self):
        # Obtener la lista de archivos CSV en el directorio de la base de datos
        archivos_csv = [archivo for archivo in os.listdir(self.db_path) if archivo.endswith('.csv')]

        # Obtener los nombres de las tablas a partir de los nombres de archivo
        nombres_tablas = [archivo[:-4] for archivo in archivos_csv]  # Eliminar la extensión .csv

        return nombres_tablas

    def count_rows_in_table(self, table_name):
        # Construir la ruta del archivo CSV
        file_path = os.path.join(self.db_path, f"{table_name}.csv")

        # Leer el archivo CSV y contar el número de filas
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            # Restamos 1 para no contar el encabezado de las columnas
            row_count = len(list(reader))-1
        return row_count
