# APP_DESCARGA_SIGED

# 📥 Sistema de Descarga de Documentos SIGED (CGR)

Este proyecto permite **automatizar la descarga de documentos PDF** desde el sistema SIGED de la Contraloría General de la República de Costa Rica. El sistema está compuesto por un **frontend en React** y un **backend en FastAPI con Playwright**. El usuario puede ingresar un enlace al documento desde una interfaz web, y el sistema automatiza la navegación y descarga del archivo.

---

## 📁 Estructura General del Proyecto --- BASE

APP_DESCARGA_SIGED/
│
├── backend/
│   └── app/
│       ├── main.py             # Arranca el servidor FastAPI
│       ├── routes.py           # Define el endpoint /descargar
│       └── DESCARGA_SIGED.py   # Script de automatización y descarga con Playwright
│
└── frontend/
└── src/
├── App.jsx             # Componente principal de React
├── App.css             # Estilos del frontend
└── main.jsx            # Punto de entrada de la app React

---

---

## 🔄 Flujo General del Sistema

```mermaid
graph TD
    A[Usuario] --> B[Frontend (App.jsx)]
    B --> C[POST URL a /descargar]
    C --> D[Backend (FastAPI)]
    D --> E[Playwright automatiza navegador]
    E --> F[Descarga PDF en carpeta local]
    F --> G[Backend devuelve estado]
    G --> B[Frontend muestra resultado]

🧠 Componentes Detallados

🔙 Backend
	•	main.py:
Inicia la aplicación FastAPI y monta las rutas del sistema.
	•	routes.py:
Define el endpoint /descargar, recibe la URL del frontend, y ejecuta la función principal del script de descarga.
	•	DESCARGA_SIGED.py:
Script principal con Playwright. Automatiza un navegador Chromium para abrir el enlace de SIGED, detectar documentos PDF y descargarlos con nombres correctos a la ruta local.

💻 Frontend
	•	App.jsx:
Muestra un formulario para ingresar una URL. Valida que la URL empiece con http, y si es válida, la envía al backend mediante fetch POST a http://localhost:8000/descargar.
	•	App.css:
Estiliza el input de URL, botón y mensajes de estado para brindar una interfaz clara y sencilla.
	•	main.jsx:
Arranque principal de la aplicación React. Renderiza <App />.

🚀 Cómo Ejecutar el Sistema

1️⃣ Iniciar el Backend

cd /Users/sultan/CGR/2025/APP_DESCARGA_SIGED/BASE/backend
uvicorn main:app --reload

2️⃣ Iniciar el Frontend

cd /Users/sultan/CGR/2025/APP_DESCARGA_SIGED/BASE/frontend
npm install      # (solo la primera vez)
npm run dev

Esto levanta el frontend en:
👉 http://localhost:5173

🧪 Cómo Probar
	1.	Abrí el navegador y accedé a: http://localhost:5173
	2.	Pegá esta URL de prueba en el formulario:

https://cgrweb.cgr.go.cr/apex/f?p=CORRESPONDENCIA:1:::::P1_CONSECUTIVO:A88C108C63FD77A3C0E96E1EE8FC6802

	3.	Presioná “Iniciar Descarga”
	4.	El backend lanzará el navegador automatizado para descargar los archivos PDF.
	5.	Los documentos se guardarán en:
/Users/sultan/Downloads/testdescarga
	6.	Por ahora, el estado de la descarga se puede observar solo en la consola del backend.

🧰 Requisitos

Backend
	•	Python 3.11+
	•	FastAPI
	•	Playwright

Instalación:

pip install fastapi uvicorn playwright
playwright install

Frontend
	•	Node.js + npm
	•	React + Vite

Instalación:

npm install

✅ Estado Actual
	•	Frontend funcional
	•	Backend operativo y ejecutando descargas reales
	•	Comunicación frontend ↔ backend exitosa
	•	Validación de URL
	•	Mostrar progreso en el frontend (pendiente para futuras mejoras)

⸻

✨ Siguiente Mejora

Agregar WebSocket o Server-Sent Events (SSE) para mostrar en tiempo real el progreso de descarga en el frontend.

