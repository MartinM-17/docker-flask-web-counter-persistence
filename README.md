# Flask Visit Tracker

## Descripción

Este proyecto implementa una aplicación web simple en Flask que registra el número de visitas a la página principal. Los datos del contador se almacenan de manera persistente usando Docker, lo que permite probar y comparar dos métodos de persistencia de datos:

- **Volúmenes de Docker:** Los datos se almacenan en un volumen independiente del contenedor.
- **Bind Mounts:** Los datos se almacenan directamente en el sistema de archivos de la máquina host.

## Estructura del Proyecto

```
flask-visit-tracker/
│
├── app.py               # Código principal de la aplicación Flask
├── Dockerfile           # Configuración para crear la imagen de Docker
├── requirements.txt     # Dependencias necesarias para la aplicación
└── data/                # Directorio donde se almacenan los datos (bind mount)
```

## Requisitos Previos

Asegúrate de tener instalados los siguientes componentes en tu máquina:

- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

## Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/MartinM-17/docker-flask-web-counter-persistence.git
cd docker-flask-web-counter-persistence
```

### 2. Crear la Imagen de Docker

Construye la imagen de Docker para la aplicación:

```bash
docker build -t flask-visit-tracker .
```

### 3. Ejecutar el Contenedor

#### a) Usando un Volumen de Docker

```bash
docker run -d -p 5000:5000 -v visit_data:/data flask-visit-tracker
```

Este comando:
- Asigna un volumen de Docker llamado `visit_data` para almacenar los datos persistentes en el contenedor.

#### b) Usando un Bind Mount

```bash
docker run -d -p 5000:5000 -v $(pwd)/data:/data flask-visit-tracker
```

Este comando:
- Usa el directorio local `./data` como bind mount para almacenar los datos persistentes.

## Uso

1. Abre tu navegador web y visita `http://localhost:5000`.
2. Cada vez que recargues la página, el contador de visitas aumentará.

## Verificar la Persistencia

### Volúmenes de Docker

1. Detén y reinicia el contenedor:
   ```bash
   docker stop <container_id>
   docker start <container_id>
   ```
2. Accede nuevamente a `http://localhost:5000` y verifica que el contador conserva su valor anterior.

### Bind Mount

1. Inspecciona directamente el archivo de datos en tu máquina local:
   ```bash
   cat ./data/counter.txt
   ```

   El archivo mostrará el valor actual del contador.

## Reiniciar el Contador

Si deseas que el contador se reinicie al reiniciar el contenedor:

1. Elimina los datos almacenados:
   - Para volúmenes: 
     ```bash
     docker volume rm visit_data
     ```
   - Para bind mounts:
     ```bash
     rm ./data/counter.txt
     ```
2. Vuelve a ejecutar el contenedor.

## Limpieza

Para eliminar la imagen y los contenedores asociados:

1. Lista los contenedores en ejecución:
   ```bash
   docker ps -a
   ```
2. Elimina los contenedores asociados:
   ```bash
   docker rm -f <container_id>
   ```
3. Elimina la imagen de Docker:
   ```bash
   docker rmi flask-visit-tracker
   ```
4. Si usaste volúmenes, elimínalos:
   ```bash
   docker volume rm visit_data
   ```
---
