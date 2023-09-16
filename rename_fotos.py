import os
from datetime import datetime
from pathlib import Path
from tqdm import tqdm
import re

# Ruta de la carpeta que contiene las fotos
ruta_base = Path(r"D:\photos\Duplicados")

# Ruta del archivo de registro
archivo_registro = Path("archivos_procesados.txt")

# Lista de extensiones de archivo válidas para fotos
extensiones_validas = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]

def obtener_fecha_modificacion(archivo):
    # Obtiene la fecha de modificación del archivo
    fecha_modificacion = datetime.fromtimestamp(archivo.stat().st_mtime)
    
    # Formatea la fecha como 'DDMMYYYY_HHMMSS'
    fecha_formateada = fecha_modificacion.strftime("%d%m%Y_%H%M%S")
    return fecha_formateada

def obtener_fecha_creacion(archivo):
    # Obtiene la fecha de creación del archivo
    fecha_creacion = datetime.fromtimestamp(archivo.stat().st_ctime)
    
    # Formatea la fecha como 'DDMMYYYY_HHMMSS'
    fecha_formateada = fecha_creacion.strftime("%d%m%Y_%H%M%S")
    return fecha_formateada

def renombrar_archivos_por_fecha(ruta_base):
    ruta_base = Path(ruta_base)
    
    # Obtiene la lista de archivos para mostrar una barra de progreso
    archivos_a_procesar = list(ruta_base.rglob('*'))
    
    nombres_registrados = obtener_archivos_procesados()

    for ruta_archivo in tqdm(archivos_a_procesar, desc="Procesando archivos"):
        if ruta_archivo.is_file() and ruta_archivo.suffix.lower() in extensiones_validas:
            # Verifica si el archivo ya tiene un nombre en el formato deseado
            nombre_archivo = ruta_archivo.name
            if re.match(r'^IMG_\d{8}_\d{6}\.\w+$', nombre_archivo):
                continue  # Ignora el archivo si ya tiene un nombre en el formato deseado

            # Obtiene la fecha para renombrar el archivo
            fecha_modificacion = obtener_fecha_modificacion(ruta_archivo)
            fecha_creacion = obtener_fecha_creacion(ruta_archivo)

            # Prioriza la fecha de modificación si está disponible
            if fecha_modificacion:
                fecha_para_renombrar = fecha_modificacion
            else:
                fecha_para_renombrar = fecha_creacion

            # Construye un nuevo nombre de archivo basado en la fecha
            nuevo_nombre = f"IMG_{fecha_para_renombrar}" + ruta_archivo.suffix
            
            # Maneja colisiones de nombres de archivo
            contador = 1
            while nuevo_nombre in nombres_registrados:
                nuevo_nombre = f"IMG_{fecha_para_renombrar}_{contador}" + ruta_archivo.suffix
                contador += 1

            nombres_registrados.add(nuevo_nombre)

            # Ruta del nuevo archivo con el nuevo nombre
            nuevo_archivo = ruta_base / nuevo_nombre

            # Verifica si el archivo con el nuevo nombre ya existe
            if not nuevo_archivo.exists():
                ruta_archivo.rename(nuevo_archivo)
                registrar_archivo_procesado(nuevo_nombre)

def obtener_archivos_procesados():
    if archivo_registro.exists():
        with open(archivo_registro, 'r') as archivo:
            return set(archivo.read().splitlines())
    else:
        return set()

def registrar_archivo_procesado(nombre_archivo):
    with open(archivo_registro, 'a') as archivo:
        archivo.write(nombre_archivo + '\n')

if __name__ == "__main__":
    renombrar_archivos_por_fecha(ruta_base)
