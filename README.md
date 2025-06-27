# APP_DESCARGA_SIGED

# 📥 Sistema de Descarga de Documentos SIGED (CGR)

Este proyecto permite **automatizar la descarga de documentos PDF** desde el sistema SIGED de la Contraloría General de la República de Costa Rica. El sistema está compuesto por un **frontend en React** y un **backend en FastAPI con Playwright**. El usuario puede ingresar un enlace al documento desde una interfaz web, y el sistema automatiza la navegación y descarga del archivo.

---------------------------------------

Este proyecto permite descargar automáticamente los documentos disponibles en el sistema SIGED de la Contraloría General de la República (CGR), ingresando una URL pública del sistema. La solución cuenta con un frontend en React y un backend en FastAPI que se comunican entre sí para gestionar la descarga y mostrar el estado de la operación.

El propósito es permitir que cualquier funcionario o persona autorizada pueda ingresar una URL del sistema SIGED y obtener de forma automática todos los documentos asociados a esa URL, sin necesidad de realizar múltiples clics ni abrir ventanas manualmente.

## 📁 Estructura General del Proyecto

El proyecto se divide en dos carpetas principales:
	•	frontend/: Contiene el código del cliente (interfaz gráfica con React).
	•	backend/: Contiene la lógica del servidor (API en FastAPI y lógica de descarga).

Dentro del backend, existe una subcarpeta llamada app/, que organiza los archivos principales de la aplicación del backend.

Estructura típica:

├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes.py
│   │   └── DESCARGA_SIGED.py
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx

¿Cómo funciona el flujo?
	1.	El usuario abre el frontend en su navegador. La interfaz ofrece un formulario donde se puede ingresar una URL válida del sistema SIGED (debe comenzar con http o https).
	2.	Al hacer clic en “Iniciar Descarga”, el frontend envía la URL al backend mediante una petición POST al endpoint /descargar/.
	3.	El backend recibe la URL y ejecuta el script DESCARGA_SIGED.py, el cual utiliza Playwright para navegar el sitio, detectar los documentos disponibles y descargarlos automáticamente a una carpeta local (/Users/sultan/Downloads/testdescarga o la ruta que se configure).
	4.	La respuesta (por ahora solo en consola) muestra mensajes de avance de la descarga: cuántos documentos se encontraron, cuáles fueron descargados, etc.
	5.	En futuras versiones, el backend emitirá mensajes en tiempo real hacia el frontend usando WebSockets para mostrar el estado directamente en la interfaz.

⸻

🧩 Componentes del Backend
	•	main.py: Archivo principal de arranque del servidor FastAPI. Crea la instancia de la aplicación e incluye las rutas definidas en routes.py.
	•	routes.py: Define el endpoint /descargar/, que recibe una URL vía POST y llama a la función descargar_documentos().
	•	DESCARGA_SIGED.py: Contiene toda la lógica de descarga usando Playwright. Abre el navegador, detecta los enlaces a documentos, descarga los archivos PDF y los guarda localmente. Incluye manejo de errores y mensajes informativos.

⸻

🧩 Componentes del Frontend (React)
	•	App.jsx: Componente principal de la aplicación React. Muestra el formulario para ingresar la URL, gestiona el estado del input y muestra mensajes de avance o error. Valida que la URL comience con http o https antes de enviarla al backend.
	•	App.css: Define el estilo visual del frontend. Mejora la presentación del formulario, botones y mensajes.
	•	main.jsx: Punto de entrada de la aplicación React. Se encarga de renderizar el componente App dentro del DOM del navegador.

⸻

🚀 ¿Cómo ejecutar el proyecto?

A continuación se detallan los pasos para levantar tanto el backend como el frontend de forma local:

1. Levantar el Backend (FastAPI)

Abrí una terminal y posicionate dentro de la carpeta backend/app. Luego ejecutá:

uvicorn main:app --reload        

Esto iniciará el servidor en http://127.0.0.1:8000.

2. Levantar el Frontend (React)

Abrí otra terminal, posicionate dentro de la carpeta frontend, y ejecutá:

npm run dev

Esto abrirá la aplicación en http://localhost:5173 (o el puerto indicado por Vite).

🧪 Prueba de funcionamiento

	1.	Ingresá una URL válida del sistema SIGED como: https://cgrweb.cgr.go.cr/apex/f?p=CORRESPONDENCIA:1:::::P1_CONSECUTIVO:A88C108C63FD77A3C0E96E1EE8FC6802

	2.	Hacé clic en “Iniciar Descarga”.
	3.	Observá los mensajes en consola donde se indicará si se cargó la página correctamente, cuántos documentos se encontraron, y si fueron descargados con éxito.

📝 Nota: La carpeta de destino de los archivos descargados es actualmente /Users/sultan/Downloads/testdescarga, pero se puede cambiar en DESCARGA_SIGED.py.

📌 Detalles adicionales
	•	Si el backend no se ejecuta, asegurate de tener instalado playwright y haber ejecutado playwright install previamente.
	•	Si querés mover este proyecto a otra computadora, recordá modificar la ruta de descarga y asegurarte que Playwright esté instalado en ese entorno.




## 📁 Mod1: carpeta de descarga.

✅ ¿Qué hace esta funcionalidad?

Permite que, al ingresar una URL del sistema SIGED o ZHED, se descarguen automáticamente los archivos correspondientes a una carpeta localizada en el directorio de descargas principal del sistema operativo, llamada: SIGED_DOCUMENTOS.

⚙️ ¿Cómo funciona?

	•	El usuario ingresa una URL en el frontend.
	•	Se valida que comience con http o https.
	•	El backend recibe la URL, lanza el proceso de descarga asincrónico utilizando Playwright.
	•	Los archivos se guardan en ~/Descargas/SIGED_DOCUMENTOS o su equivalente según el sistema operativo:
	•	Windows: C:\Users\Usuario\Downloads\SIGED_DOCUMENTOS
	•	macOS/Linux: /Users/usuario/Downloads/SIGED_DOCUMENTOS o /home/usuario/Downloads/SIGED_DOCUMENTOS

🔧 Cambios realizados

🧠 Backend (/backend/app)

	•	Nuevo módulo creado: DESCARGA_SIGED.py
	•	Función principal: descargar_documentos(url, ruta_descarga)
	•	Utiliza Playwright para automatizar y realizar la descarga.
	•	Determina automáticamente la ruta de descarga con platformdirs.user_downloads_dir().
	•	Modificado: routes.py
	•	Ruta POST /descargar
	•	Crea una tarea asincrónica con asyncio.create_task(...) para llamar a descargar_documentos(...).

🎨 Frontend (/frontend/src)

	•	Modificado: App.jsx
	•	Se eliminó el input de “Carpeta de destino”.
	•	Se agregó un mensaje fijo indicando que los archivos se descargarán en la carpeta SIGED_DOCUMENTOS dentro del directorio de descargas.
	•	Estructura visual mantenida exactamente como estaba.

📁 Scripts principales modificados

	•	app/DESCARGA_SIGED.py: Archivo nuevo. Contiene toda la lógica de descarga utilizando automatización con ruta inteligente.
	•	app/routes.py: Se añadió una nueva ruta POST /descargar que invoca el módulo de descarga.
	•	src/App.jsx: La interfaz de usuario fue adaptada para eliminar el input de carpeta de destino. En su lugar, ahora se muestra un mensaje estático indicando que los archivos se descargarán automáticamente en la carpeta SIGED_DOCUMENTOS.











