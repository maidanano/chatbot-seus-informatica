import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATOS_DIR = BASE_DIR / "datos"

ARCHIVO_ORDENES = DATOS_DIR / "ordenes.txt"
ARCHIVO_CONSULTAS = DATOS_DIR / "consultas.txt"
ARCHIVO_AVISOS = DATOS_DIR / "avisos_tecnicos.txt"

#Carga las órdenes desde un archivo TXT con formato CSV.
def cargar_ordenes():
    
    ordenes = []

    try:
        with open(ARCHIVO_ORDENES, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                if fila.get("orden") and fila.get("cliente") and fila.get("estado"):
                    ordenes.append({
                        "orden": fila["orden"].strip(),
                        "cliente": fila["cliente"].strip(),
                        "telefono": fila["telefono"].strip(),
                        "equipo": fila["equipo"].strip(),
                        "falla": fila["falla"].strip(),
                        "estado": fila["estado"].strip(),
                        "tecnico_asignado": fila["tecnico_asignado"].strip()
                    })

    except FileNotFoundError:
        print("Error: no se encontró el archivo de órdenes.")
    except PermissionError:
        print("Error: no hay permisos para leer el archivo de órdenes.")
    except Exception as error:
        print(f"Error al cargar órdenes: {error}")

    return ordenes


#Busca una orden específica por su número de orden.
def buscar_por_orden(ordenes, numero_orden):
    for orden in ordenes:
        if orden["orden"] == numero_orden:
            return orden

    return None


#Busca órdenes por el nombre del cliente.
def buscar_por_nombre(ordenes, nombre):
    nombre = nombre.lower()
    resultados = []

    for orden in ordenes:
        if nombre in orden["cliente"].lower():
            resultados.append(orden)

    return resultados

#Busca órdenes por el estado del servicio.
def registrar_consulta(cliente, tipo_consulta, dato_ingresado, resultado):
    try:
        existe_archivo = ARCHIVO_CONSULTAS.exists()

        with open(ARCHIVO_CONSULTAS, "a", encoding="utf-8", newline="") as archivo:
            campos = ["fecha", "cliente", "tipo_consulta", "dato_ingresado", "resultado"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if not existe_archivo or ARCHIVO_CONSULTAS.stat().st_size == 0:
                escritor.writeheader()

            escritor.writerow({
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "cliente": cliente,
                "tipo_consulta": tipo_consulta,
                "dato_ingresado": dato_ingresado,
                "resultado": resultado
            })

            print("Enviando consulta al técnico.... Gracias por tu paciencia!")

    except Exception as error:
        print(f"No se pudo registrar la consulta: {error}")

#Registra un aviso técnico con los detalles del cliente, orden, equipo, motivo y técnico asignado.
def registrar_aviso(cliente, orden, equipo, motivo, tecnico_asignado):
    try:
        existe_archivo = ARCHIVO_AVISOS.exists()

        with open(ARCHIVO_AVISOS, "a", encoding="utf-8", newline="") as archivo:
            campos = ["fecha", "cliente", "orden", "equipo", "motivo", "tecnico_asignado"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if not existe_archivo or ARCHIVO_AVISOS.stat().st_size == 0:
                escritor.writeheader()

            escritor.writerow({
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "cliente": cliente,
                "orden": orden,
                "equipo": equipo,
                "motivo": motivo,
                "tecnico_asignado": tecnico_asignado
            })

    except Exception as error:
        print(f"No se pudo registrar el aviso técnico: {error}")
