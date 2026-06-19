# Chatbot SEUS Informática

Simulador de chatbot para atención inicial de consultas por WhatsApp en SEUS Informática.

## Objetivo

Automatizar consultas frecuentes, consultar estados de órdenes de servicio y derivar al técnico del área cuando sea necesario.

## Ejecución

Desde la carpeta principal del proyecto:

```bash
python main.py
```

## Estructura

```text
chatbot-seus-informatica/
├── main.py
├── datos/
│   ├── ordenes.txt
│   ├── consultas.txt
│   └── avisos_tecnicos.txt
├── modulos/
│   ├── bot.py
│   ├── base_datos.py
│   ├── validaciones.py
│   ├── estados.py
│   └── mensajes.py
└── README.md
```

## Funcionalidades

- Menú principal por consola.
- Consulta de estado por número de orden.
- Búsqueda alternativa por nombre o apellido.
- Respuesta automática para estados finales.
- Derivación al técnico para estados activos.
- Registro de consultas y avisos en archivos TXT con formato CSV.
- Manejo de errores mediante validaciones y bloques `try/except`.

## Estados de órdenes

Respuesta automática:

- Lista
- No aceptado
- Sin solución

Derivación al técnico:

- Pendiente
- Cotizada
- Aceptada
