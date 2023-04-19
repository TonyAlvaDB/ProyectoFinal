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
            row_count = len(list(reader))
        return row_count
    
    def get_full_list(self, table_name) -> list:
        file_path = os.path.join(self.db_path, f"{table_name}.csv")
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
            return data
        
    def get_just_names (self) -> list:
        tablaCompleta = self.get_full_list("CDP")
        tablaNombres = []
        for x in tablaCompleta:
            tablaNombres.append(x[0])
        return tablaNombres
    
    def transfer_item(self, source_table_name, destination_table_name, item_name, quantity):
        tabla1 = os.path.join(self.db_path, f"{source_table_name}.csv")
        tabla2 = os.path.join(self.db_path, f"{destination_table_name}.csv")
        
        informacionBodegaSource = self.get_full_list(source_table_name)
        informacionBodegaDestino = self.get_full_list(destination_table_name)
        
        for x in range(self.count_rows_in_table(source_table_name)):
            if informacionBodegaSource[x][0] == item_name:
                cantidad1 = int(informacionBodegaSource[x][2])
                cantidad2 = int(informacionBodegaDestino[x][2])
                cantidadNueva1 = cantidad1 - quantity
                cantidadNueva2 = cantidad2 + quantity
                informacionBodegaSource[x][2] = cantidadNueva1
                informacionBodegaDestino[x][2] = cantidadNueva2

                with open(tabla1, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for row in informacionBodegaSource:
                        writer.writerow(row)

                with open(tabla2, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    for row in informacionBodegaDestino:
                        writer.writerow(row)
                print("La información ha sido enviada exitosamente")
                break