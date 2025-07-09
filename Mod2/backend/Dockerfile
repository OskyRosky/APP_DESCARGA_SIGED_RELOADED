# Imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del backend al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que utilizará Uvicorn
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["uvicorn", "app.routes:app", "--host", "0.0.0.0", "--port", "8000"]