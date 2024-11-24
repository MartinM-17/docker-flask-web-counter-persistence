# Usamos una imagen base de Python 3.9 que es ligera y eficiente
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos de la aplicación desde el directorio actual al contenedor
COPY . /app

# Instalamos las dependencias especificadas en el archivo requirements.txt.
# - `--no-cache-dir`: Evita que pip almacene en caché los archivos temporales de instalación, reduciendo el tamaño de la imagen.
# - `-r requirements.txt`: Indica a pip que lea la lista de paquetes desde el archivo `requirements.txt`.
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos al contenedor
COPY . .

# Exponemos el puerto 5000 para que Flask pueda comunicarse con el mundo exterior
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
