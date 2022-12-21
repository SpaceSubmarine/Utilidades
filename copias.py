import os
import shutil
# Script para hacer copias de dos discos duros sin duplicados

# Nombres de los discos duros de origen
disk1 = "C:"
disk2 = "D:"

# Nombre del disco duro de destino
disk3 = "E:"

# Creamos una lista de archivos copiados para comprobar si ya existen
copied_files = []

# Recorremos los archivos de los discos duros de origen
for root, dirs, files in os.walk(disk1):
    for file in files:
        # Si el archivo no ha sido copiado anteriormente, lo copiamos al disco duro de destino
        if file not in copied_files:
            shutil.copy(os.path.join(root, file), disk3)
            # Añadimos el archivo a la lista de archivos copiados
            copied_files.append(file)

for root, dirs, files in os.walk(disk2):
    for file in files:
        if file not in copied_files:
            shutil.copy(os.path.join(root, file), disk3)
            copied_files.append(file)

print("Copia completada con éxito")