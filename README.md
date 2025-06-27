# APP_DESCARGA_SIGED

## Base del proyecto

🧩 Descripción del Proyecto

Este proyecto permite descargar automáticamente documentos PDF desde el sistema SIGED (Sistema de Gestión Documental de la CGR de Costa Rica), a partir de un enlace compartido. La solución está compuesta por un frontend en React y un backend en FastAPI con Playwright, que interactúan de forma asíncrona mediante HTTP.

📁 Estructura General

El proyecto está dividido en dos carpetas principales:

/backend
  └── app
       ├── DESCARGA_SIGED.py
       ├── routes.py
       └── main.py
/frontend
  ├── src
       ├── App.jsx
       ├── App.css
       └── main.jsx

⚙️ ¿Cómo funciona el sistema?
	1.	El usuario ingresa una URL válida del sistema SIGED desde el frontend.
	2.	El frontend envía esa URL al backend mediante una petición POST a un endpoint /descargar.
	3.	El backend ejecuta Playwright para automatizar la navegación, abrir los documentos y descargarlos.
	4.	Los archivos PDF se guardan localmente en una carpeta especificada (como Downloads/testdescarga).
	5.	El estado de la descarga se muestra en el frontend.


🧠 Componentes del Backend (FastAPI + Playwright)

📁 app/DESCARGA_SIGED.py
	•	Es el núcleo del sistema de descarga.
	•	Usa playwright.async_api para automatizar el navegador.
	•	Accede a la URL proporcionada, detecta enlaces de documentos, los abre en ventanas emergentes y descarga los archivos PDF.
	•	Permite enviar mensajes de estado (print o await notificar()) para usarlos en terminal o transmitir a frontend.

📄 app/routes.py
	•	Define los endpoints de la API.
	•	Expone un endpoint /descargar que recibe una URL en formato JSON.
	•	Llama a la función descargar_documentos() y procesa la respuesta.
	•	Esta es la puerta de entrada para que el frontend se comunique con el backend.

🚀 app/main.py
	•	Arranca el servidor FastAPI.
	•	Incluye las rutas definidas en routes.py.
	•	Es el punto de entrada del backend.

Ejemplo para ejecutarlo:


uvicorn app.main:app --reload

💻 Componentes del Frontend (React)

⚙️ App.jsx
	•	Es la interfaz principal.
	•	Tiene un formulario con un input de tipo texto para ingresar la URL del documento.
	•	Al presionar el botón “Iniciar Descarga”, se hace un fetch POST a http://localhost:8000/descargar.
	•	Muestra mensajes de estado y validación (por ejemplo, si la URL no comienza con http o https).

⸻

🎨 App.css
	•	Contiene los estilos visuales del formulario.
	•	Aplica diseño básico a los inputs, botones y mensajes.

⸻

🔁 main.jsx
	•	Es el archivo de entrada principal de React.
	•	Renderiza el componente App dentro del div#root.

⸻

🔗 Flujo de Interacción Completo

graph TD
    A[Usuario] --> B[Frontend (App.jsx)]
    B --> C[POST URL a /descargar]
    C --> D[Backend (FastAPI)]
    D --> E[Playwright automatiza navegador]
    E --> F[Se descargan PDFs localmente]
    F --> G[Backend responde estado]
    G --> B[Frontend muestra resultado]

✅ ¿Qué hace el usuario?
	1.	Abre el frontend en el navegador (http://localhost:5173 o similar).
	2.	Pega una URL válida del SIGED (por ejemplo, la que contiene P1_CONSECUTIVO=...).
	3.	Presiona “Iniciar Descarga”.
	4.	Se activa el backend, el navegador se abre automáticamente, los documentos se descargan.
	5.	El usuario ve el estado de la operación en pantalla (y más adelante, se podrá mostrar el progreso en tiempo real).

🛠 Requisitos técnicos

Backend
	•	Python 3.11+
	•	FastAPI
	•	Playwright (con Chromium instalado)
	•	Uvicorn

Frontend
	•	Node.js + npm
	•	Vite + React


## Propotipo I










 
