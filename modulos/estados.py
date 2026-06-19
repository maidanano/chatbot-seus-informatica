# Estados posibles de una orden de servicio

ESTADOS_RESPUESTA_AUTOMATICA = ["Lista", "No aceptado", "Sin solución"]
ESTADOS_DERIVACION_TECNICO = ["Pendiente", "Cotizada", "Aceptada"]

ESTADOS_VALIDOS = ESTADOS_RESPUESTA_AUTOMATICA + ESTADOS_DERIVACION_TECNICO


def requiere_tecnico(estado):
    """Devuelve True si el estado requiere intervención del técnico."""
    return estado in ESTADOS_DERIVACION_TECNICO


def es_estado_final(estado):
    """Devuelve True si el estado permite una respuesta automática."""
    return estado in ESTADOS_RESPUESTA_AUTOMATICA
