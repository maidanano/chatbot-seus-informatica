# Mensajes utilizados por el chatbot


def mostrar_bienvenida():
    print("\n----------------------------------------")
    print("CHATBOT SEUS INFORMÁTICA")
    print("----------------------------------------")
    print("Hola, soy Rango,el asistente virtual de SEUS Informática.")


def mostrar_menu():
    print("\n¿Cómo puedo ayudarte?")
    print("1. Consultar estado de un equipo")
    print("2. Consultar horarios y dirección")
    print("3. Consultar si reparamos un equipo")
    print("4. Consultar por recarga de tóner o impresoras")
    print("5. Consultar por insumos")
    print("6. Solicitar asistencia remota")
    print("7. Hablar con un técnico")
    print("0. Salir")

#Mensaje para consultas sobre el estado de un equipo, con respuestas personalizadas según el estado registrado en la orden.
def mensaje_estado(orden):
    estado = orden["estado"]
    equipo = orden["equipo"]
    orden_numero = orden["orden"]

    if estado == "Lista":
        return (
            f"La orden {orden_numero}, correspondiente a {equipo}, figura como LISTA.\n"
            "El equipo ya está disponible para retirar.\n"
            "Podes retirarla de lunes a viernes de 8:00 a 12:30 hs y de 16:00 a 20:00 hs, en Maipú 1113. Gracias!"
        )

    if estado == "No aceptado":
        return (
            f"La orden {orden_numero}, correspondiente a {equipo}, figura como NO ACEPTADA.\n"
            "El presupuesto no fue aceptado, por lo tanto puede pasar a retirar el equipo sin costo dentro de nuestros horarios de atención."
        )

    if estado == "Sin solución":
        return (
            f"La orden {orden_numero}, correspondiente a {equipo}, figura como SIN SOLUCIÓN.\n"
            "El equipo fue revisado, pero no pudo resolverse la falla. Puede pasar a retirarlo por nuestro sin cargo en nuestros horarios de  atención. Gracias!"
        )

    if estado == "Pendiente":
        return (
            f"La orden {orden_numero}, correspondiente a {equipo}, se encuentra PENDIENTE.\n"
            "Ya avisé al técnico del área para que se comunique con vos a la brevedad por las novedades de tu equipo. Gracias!"
        )

    if estado == "Cotizada":
        return (
            f"La orden {orden_numero}, correspondiente a {equipo}, ya fue COTIZADA.\n"
            "Un técnico del área se comunicará a la brevedad para informarte los detalles y novedades de tu equipo. Gracias!"
        )

    if estado == "Aceptada":
        return (
            f"La orden {orden_numero}, correspondiente a {equipo}, figura como ACEPTADA.\n"
            "El equipo continúa en gestión técnica. Ya registramos el aviso para el técnico del área.\n"
            "Un técnico del área se comunicará a la brevedad para informarte los detalles y novedades de tu equipo. Gracias!"
        )

    return "No pude interpretar el estado de la orden solicitada. derivaré la consulta al técnico del área.\n" \
    "Un técnico del área se comunicará a la brevedad para informarte los detalles y novedades de tu equipo. Gracias!"


#Mensaje para consultas que no arrojan resultados.
def mensaje_no_encontrado():
    return (
        "No encontré una orden con esos datos.\n"
        "Voy a registrar la consulta para que una persona del local pueda revisar el caso y se comunique con vos a la brevedad. Gracias!"
    )

#Mensaje para consultas que arrojan varias órdenes asociadas al mismo nombre.
def mensaje_varias_ordenes():
    return (
        "Encontré varias órdenes asociadas a ese nombre.\n"
        "Para evitar informar datos incorrectos, registré un aviso para que el técnico del área revise el caso y se comunique con vos a la brevedad. Gracias!"
    )

#Mensaje para consultas sobre horarios y dirección del local.
def mensaje_horarios():
    return "Atendemos de lunes a viernes de 8:00 a 12:30 hs y de 16:00 a 20:00 hs. Estamos en Maipú 1113.\n Gracias por consultar!"

#Mensaje para consultas sobre reparaciones de equipos.
def mensaje_reparaciones():
    return (
        "Realizamos servicio técnico de computadoras, notebooks, impresoras, televisores, cargadores "
        "y otros equipos electrónicos. Podés acercar el equipo al local para una revisión y presupuesto sin cargo."
        "Gracias por consultar!"
    )

#Mensaje para consultas sobre recarga de tóner o reparación de impresoras.
def mensaje_toner():
    return (
        "Realizamos reparación de impresoras y recarga de tóner. "
        "Para confirmar el trabajo, podés acercarte al local o aguardar la respuesta del técnico del área."
    )

#Mensaje para consultas sobre insumos.
def mensaje_derivacion():
    return "Registré tu consulta. Una persona del local se comunicará a la brevedad para brindarte más detalles. Gracias por consultar!"
