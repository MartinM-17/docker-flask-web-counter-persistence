# Importamos las librerías necesarias
from flask import Flask # Flask es el framework web ligero para Python
import os               # Para interactuar con el sistema de archivos del contenedor

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos el directorio donde guardaremos el archivo de contadores
data_dir = "/data"

# Verificamos si el directorio donde almacenaremos los datos existe; si no, lo creamos
if not os.path.exists(data_dir):
    os.makedirs(data_dir)  # Crea el directorio /data si no existe

# Definimos una ruta para la página principal
@app.route('/')
def home():
    """
    Función principal que se ejecuta cuando se accede a la página raíz (/).
    Incrementa un contador de visitas y lo guarda en un archivo.
    """

    # Especificamos la ubicación del archivo de contador
    counter_file = os.path.join(data_dir, 'counter.txt')
    
    # Leemos el contador de visitas desde el archivo (si ya existe)
    if os.path.exists(counter_file):
        # Si el archivo existe, abrimos y leemos el valor actual del contador
        with open(counter_file, 'r') as f:
            count = int(f.read().strip())  # Convertimos el valor leído a un número entero
    else:
        # Si el archivo no existe, comenzamos el conteo desde cero
        count = 0
    
    # Incrementamos el contador
    count += 1

    # Guardamos el nuevo valor del contador en el archivo
    with open(counter_file, 'w') as f:
        f.write(str(count))  # Escribimos el contador actualizado en el archivo
    
    # Retornamos la cantidad actual de visitas como respuesta al usuario
    return f"Visitas: {count}"

# Ejecutamos la aplicación Flask
if __name__ == '__main__':
    """
    Punto de entrada de la aplicación. Inicia el servidor web de Flask para que
    escuche en todas las interfaces de red (host=0.0.0.0) en el puerto 5000.
    """
    app.run(host='0.0.0.0', port=5000)
