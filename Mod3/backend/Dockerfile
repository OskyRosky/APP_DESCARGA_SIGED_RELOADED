# Usar imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la app (ajustado correctamente)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]