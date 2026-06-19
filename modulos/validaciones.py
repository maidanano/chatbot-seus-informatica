# Funciones de validación de entradas


def pedir_opcion_menu():
    while True:
        try:
            opcion = input("\nIngresá una opción: ").strip()

            if opcion == "":
                raise ValueError("Para poder ayudarte tenés que ingresar una opción. Gracias")

            opcion = int(opcion)

            if opcion < 0 or opcion > 7:
                raise ValueError("La opción que elijas, debe estar entre 0 y 7.")

            return opcion

        except ValueError as error:
            print(f"Error: Ingresaste un valor que no es un número válido o no está dentro del rango permitido. {error}")


def pedir_texto_no_vacio(mensaje):
    while True:
        try:
            texto = input(mensaje).strip()

            if texto == "":
                raise ValueError("Para poder ayudarte, el dato no puede estar vacío. Gracias")

            return texto

        except ValueError as error:
            print(f"Error: Ingresaste un valor que no es válido. {error}")


def validar_orden(orden):
    if orden.strip() == "":
        return False

    return orden.strip().isdigit()


def normalizar_texto(texto):
    return texto.strip().lower()
