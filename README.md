# Chatbot SEUS Informática

Simulador de chatbot para la atención inicial de consultas por WhatsApp en SEUS Informática (un local de servicios técnico).

## Descripción

Este proyecto fue desarrollado como parte del Trabajo Práctico Integrador de la materia Organización Empresarial de la Universidad Tecnológica Nacional. El objetivo es simular una solución tecnológica para mejorar el proceso de atención inicial de consultas en un local de informática.

El chatbot permite responder consultas frecuentes, consultar el estado de órdenes de servicio mediante una base de datos simulada y derivar al técnico del área cuando la consulta requiere intervención humana.

## Alcance y metodología

Este proyecto es una prueba preliminar del chatbot. No está integrado a WhatsApp real ni a una base de datos productiva, sino que simula el proceso mediante una aplicación por consola y archivos `.txt` con formato CSV.

La metodología consiste en utilizar datos ficticios de órdenes de servicio para validar el comportamiento esperado: mostrar un menú, recibir datos del usuario, consultar órdenes, responder según el estado registrado y derivar al técnico del área cuando corresponde.

Se espera que el sistema responda consultas simples, permita buscar órdenes por número o nombre, informe estados finales y registre derivaciones cuando la consulta requiera intervención humana.

## Objetivo

Automatizar parte de la atención inicial para reducir respuestas repetitivas, ordenar las consultas recibidas y mejorar la trazabilidad de los pedidos realizados por los clientes. De esta manera se libera tiempo del técnico para poder realizar otras actividades.

## Funcionalidades principales

- Menú interactivo por consola.
- Consulta de estado de equipos por número de orden.
- Búsqueda alternativa por nombre o apellido.
- Respuestas automáticas para órdenes finalizadas.
- Derivación al técnico para órdenes pendientes, cotizadas o aceptadas.
- Registro de consultas realizadas.
- Registro de avisos técnicos.
- Manejo de errores y validaciones mediante `try/except`.
- Uso de archivos `.txt` con formato CSV como base de datos simulada.

## Estados de órdenes

El sistema trabaja con los siguientes estados:

- `Pendiente`: requiere intervención del técnico.
- `Cotizada`: requiere intervención del técnico.
- `Aceptada`: requiere intervención del técnico.
- `Lista`: permite informar que el equipo puede retirarse.
- `No aceptado`: permite informar que el equipo puede retirarse sin costo.
- `Sin solución`: permite informar que el equipo fue revisado y puede retirarse sin cargo.

## Estructura del proyecto

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

Descripción de archivos
main.py: archivo principal del programa.
bot.py: contiene el flujo principal del chatbot.
base_datos.py: gestiona la lectura y escritura de archivos.
validaciones.py: contiene funciones para validar entradas del usuario.
estados.py: define los estados de las órdenes.
mensajes.py: centraliza los mensajes mostrados por el chatbot.
ordenes.txt: base de datos simulada con órdenes ficticias.
consultas.txt: registro de consultas realizadas.
avisos_tecnicos.txt: registro de derivaciones al técnico del área.
Cómo ejecutar el proyecto
Descargar o clonar el repositorio.
Abrir la carpeta del proyecto en Visual Studio Code.
Ejecutar el archivo principal desde la terminal:
python main.py

En caso de usar Windows y que el comando anterior no funcione, probar con:

py main.py
Uso del sistema

Al ejecutar el programa, el chatbot muestra un menú principal con distintas opciones de consulta. El usuario debe ingresar el número correspondiente a la opción deseada.

Si elige la opción 1, podrá consultar el estado de un equipo ingresando el número de orden. Si no recuerda el número, el sistema permite buscar por nombre o apellido. Según el estado registrado en la base simulada, el bot responde automáticamente o deriva la consulta al técnico del área.

Las consultas realizadas y las derivaciones se guardan en los archivos consultas.txt y avisos_tecnicos.txt, permitiendo dejar registro de la interacción.

Datos simulados

El archivo ordenes.txt contiene datos ficticios de clientes y órdenes de servicio. Estos datos se utilizan únicamente para probar el funcionamiento del chatbot y no corresponden a clientes reales.

Relación con el proceso BPMN

El chatbot representa el proceso TO-BE propuesto en el informe. La lógica del programa se basa en el flujo modelado con BPMN 2.0, donde el sistema actúa como primer filtro de atención, responde consultas simples y deriva al técnico cuando corresponde.

Autor

Mariano Maidana
Tecnicatura Universitaria en Programación
Organización Empresarial
├── docs/
│   └── diccionario_datos.md
├── README.md
└── .gitignore
