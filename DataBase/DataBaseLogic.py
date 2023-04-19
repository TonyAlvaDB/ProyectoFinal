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
    
    def transfer_item(self, source_table, destination_table, item_name, quantity):
        source_file = os.path.join(self.db_path, f"{source_table}.csv")
        destination_file = os.path.join(self.db_path, f"{destination_table}.csv")

        if os.path.exists(source_file) and os.path.exists(destination_file):
            # Leer los datos de la tabla de origen
            source_data = self.get_full_list(source_table)

            # Buscar el índice de la fila que contiene el nombre del artículo en la tabla de origen
            source_row_index = None
            for i in range(len(source_data)):
                if source_data[i][0] == item_name:
                    source_row_index = i
                    break

            if source_row_index is not None:
                # Verificar si hay suficiente cantidad del artículo en la tabla de origen
                if int(source_data[source_row_index][1]) >= quantity:
                    # Leer los datos de la tabla de destino
                    destination_data = self.get_full_list(destination_table)

                    # Buscar el índice de la fila que contiene el nombre del artículo en la tabla de destino
                    destination_row_index = None
                    for i in range(len(destination_data)):
                        if destination_data[i][0] == item_name:
                            destination_row_index = i
                            break

                    if destination_row_index is not None:
                        # Actualizar la cantidad del artículo en la tabla de origen y de destino
                        source_data[source_row_index][1] = int(source_data[source_row_index][1]) - quantity
                        destination_data[destination_row_index][1] = int(destination_data[destination_row_index][1]) + quantity

                        # Escribir los datos actualizados en los archivos CSV
                        with open(source_file, 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(source_data)
                        with open(destination_file, 'w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(destination_data)

                        print(f"Se transfirieron {quantity} unidades del artículo '{item_name}' de la tabla '{source_table}' a la tabla '{destination_table}' exitosamente.")
                    else:
                        print(f"No se encontró el artículo '{item_name}' en la tabla '{destination_table}'.")
                else:
                    print(f"No hay suficiente cantidad del artículo '{item_name}' en la tabla '{source_table}'.")
            else:
                print(f"No se encontró el artículo '{item_name}' en la tabla '{source_table}'.")
        else:
            print(f"Una o ambas tablas '{source_table}' y '{destination_table}' no existen.")

    