from modulos.base_datos import (
    cargar_ordenes,
    buscar_por_orden,
    buscar_por_nombre,
    registrar_consulta,
    registrar_aviso
)
from modulos.validaciones import pedir_opcion_menu, pedir_texto_no_vacio, validar_orden
from modulos.estados import requiere_tecnico, ESTADOS_DERIVACION_TECNICO
from modulos.mensajes import (
    mostrar_bienvenida,
    mostrar_menu,
    mensaje_estado,
    mensaje_no_encontrado,
    mensaje_varias_ordenes,
    mensaje_horarios,
    mensaje_reparaciones,
    mensaje_toner,
    mensaje_derivacion
)


def iniciar_chatbot():
    ordenes = cargar_ordenes()

    if not ordenes:
        print("No hay órdenes cargadas. Revisá el archivo datos/ordenes.txt")
        return

    mostrar_bienvenida()
    salir = False

    while not salir:
        mostrar_menu()
        opcion = pedir_opcion_menu()

        if opcion == 0:
            print("\nGracias por comunicarte con SEUS Informática. ¡Hasta luego!")
            salir = True

        elif opcion == 1:
            consultar_estado_equipo(ordenes)

        elif opcion == 2:
            print("\n" + mensaje_horarios())
            registrar_consulta("Sin identificar", "Horarios y dirección", "Opción 2", "Respondida automáticamente")
        #Registra consultas generales sobre reparaciones, recarga de tóner o insumos, derivando al técnico del área cuando corresponde.
        elif opcion == 3:
            print("\n" + mensaje_reparaciones())
            registrar_consulta("Sin identificar", "Reparación de equipos", "Opción 3", "Respondida automáticamente")

        elif opcion == 4:
            print("\n" + mensaje_toner())
            registrar_consulta("Sin identificar", "Recarga de tóner o impresoras", "Opción 4", "Respondida automáticamente")

        elif opcion == 5:
            detalle = pedir_texto_no_vacio("\nIndicame qué insumo necesitás consultar: ")
            print("\n" + mensaje_derivacion())
            registrar_consulta("Sin identificar", "Consulta por insumos", detalle, "Derivada")
            registrar_aviso("Sin identificar", "", "", f"Consulta por insumo: {detalle}", "Atención / ventas")

        elif opcion == 6:
            detalle = pedir_texto_no_vacio("\nDescribime brevemente el problema para asistencia remota: ")
            print("\n" + mensaje_derivacion())
            registrar_consulta("Sin identificar", "Asistencia remota", detalle, "Derivada")
            registrar_aviso("Sin identificar", "", "", f"Asistencia remota: {detalle}", "Computadoras")

        elif opcion == 7:
            nombre = pedir_texto_no_vacio("\nPasametu nombre para registrar el pedido de contacto: ")
            print("\n" + mensaje_derivacion())
            registrar_consulta(nombre, "Hablar con técnico", nombre, "Derivada")
            registrar_aviso(nombre, "", "", "Pedido para hablar con técnico", "Técnico del área")


def consultar_estado_equipo(ordenes):
    print("\nConsulta de estado de equipo")
    print("Podés ingresar número de orden. Si no te lo acordás, dejalo vacío y buscá por nombre.")

    orden_ingresada = input("Número de orden: ").strip()

    if orden_ingresada != "":
        if validar_orden(orden_ingresada):
            orden = buscar_por_orden(ordenes, orden_ingresada)

            if orden:
                procesar_orden_encontrada(orden, "Búsqueda por orden", orden_ingresada)
                return

            print("\nNo encontré esa orden. Voy a intentar buscar por nombre.")
        else:
            print("\nEl número de orden que ingresaste no es válido. Voy a buscar por nombre.")

    nombre = pedir_texto_no_vacio("Ingresá nombre o apellido asociado al equipo: ")
    resultados = buscar_por_nombre(ordenes, nombre)

    if len(resultados) == 0:
        print("\n" + mensaje_no_encontrado())
        registrar_consulta(nombre, "Estado de equipo", nombre, "No encontrado - derivado")
        registrar_aviso(nombre, "", "", "No se encontré orden asociada", "Técnico del área")

    elif len(resultados) == 1:
        procesar_orden_encontrada(resultados[0], "Búsqueda por nombre", nombre)

    else:
        procesar_varias_ordenes(resultados, nombre)


def procesar_orden_encontrada(orden, tipo_consulta, dato_ingresado):
    print("\n" + mensaje_estado(orden))

    registrar_consulta(
        orden["cliente"],
        tipo_consulta,
        dato_ingresado,
        f"Estado informado: {orden['estado']}"
    )

    if requiere_tecnico(orden["estado"]):
        registrar_aviso(
            orden["cliente"],
            orden["orden"],
            orden["equipo"],
            f"Orden en estado {orden['estado']}",
            orden["tecnico_asignado"]
        )


def procesar_varias_ordenes(resultados, nombre):
    ordenes_activas = []

    for orden in resultados:
        if orden["estado"] in ESTADOS_DERIVACION_TECNICO:
            ordenes_activas.append(orden)

    if len(ordenes_activas) == 1:
        procesar_orden_encontrada(ordenes_activas[0], "Búsqueda por nombre", nombre)
    else:
        print("\n" + mensaje_varias_ordenes())
        registrar_consulta(nombre, "Estado de equipo", nombre, "Varias órdenes - derivado")

        for orden in resultados:
            registrar_aviso(
                orden["cliente"],
                orden["orden"],
                orden["equipo"],
                "Varias órdenes asociadas al mismo cliente",
                orden["tecnico_asignado"]
            )
