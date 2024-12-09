
# Guía para Configurar y Usar la Imagen Docker de Nextcloud

Esta imagen Docker ha sido diseñada para facilitar la configuración de Nextcloud en un entorno de desarrollo. Fue desarrollada por **Ricardo Rosero**.

## Descripción de la Imagen Docker

La imagen Docker de Nextcloud se basa en PHP 8.1 con Apache y contiene las extensiones necesarias para ejecutar Nextcloud de manera eficiente. Incluye las configuraciones de Apache necesarias para el funcionamiento de Nextcloud y está preconfigurada para ser utilizada con una base de datos **MariaDB**.

## Información del Desarrollador

- **Desarrollador:** Ricardo Rosero
- **Versión de la Imagen:** 1.0
- **Repositorio:** [GitHub - rr-n4p5t3r](https://github.com/rr-n4p5t3r)
- **Correo de contacto:** [rrosero2000@gmail.com](mailto:rrosero2000@gmail.com)

---

## Instrucciones para Configurar y Usar la Imagen Docker

### 1. Descargar la Imagen Docker

Primero, descarga la imagen Docker desde el siguiente enlace:

[Descargar la imagen Docker de Nextcloud](https://nube.rrsolucionesit.com/index.php/s/dCC3xSKkjgBH6TM)

Una vez descargado, tendrás un archivo `rr_nextcloud.tar` en tu sistema.

### 2. Cargar la Imagen Docker en tu Sistema

Para cargar la imagen en tu sistema local, ejecuta el siguiente comando:

```bash
docker load -i docker_images/rr_nextcloud.tar
```

Este comando cargará la imagen en tu máquina local, y podrás usarla inmediatamente.

### 3. Correr el Contenedor de Nextcloud

Una vez que la imagen ha sido cargada, puedes correr el contenedor utilizando el siguiente comando:

```bash
docker run -d -p 8080:80 nextcloud:latest
```

Esto expondrá Nextcloud en el puerto `8080` de tu máquina local. Ahora podrás acceder a Nextcloud desde el navegador visitando:

```
http://localhost:8080
```

### 4. Usar Docker Compose para Configuración Automática (Opcional)

Si prefieres configurar Nextcloud y la base de datos automáticamente utilizando Docker Compose, sigue estos pasos:

1. **Asegúrate de tener Docker Compose instalado.** Si no lo tienes, sigue la [guía oficial de Docker Compose](https://docs.docker.com/compose/install/) para instalarlo.

2. **Clona o descarga el repositorio del proyecto** en tu máquina local y navega hasta el directorio donde se encuentran los archivos `Dockerfile`, `docker-compose.yml`, y `apache-config.conf`.

3. **Construir y correr los contenedores** utilizando Docker Compose:

```bash
docker-compose up -d
```

Este comando descargará las imágenes necesarias (si aún no las tienes), construirá el contenedor de Nextcloud y el contenedor de MariaDB, y los ejecutará en segundo plano.

4. **Accede a Nextcloud** desde tu navegador visitando:

```
http://localhost:8080
```

---

### 5. Configurar Nextcloud

Una vez que hayas accedido a Nextcloud en tu navegador, sigue el asistente de instalación para configurar tu cuenta de administrador, conexión con la base de datos y otros parámetros básicos.

- **Usuario de la base de datos:** `nextcloud_user`
- **Contraseña de la base de datos:** `nextcloud_password`
- **Base de datos:** `nextcloud`
- **Host de la base de datos:** `db` (esto es debido a la configuración del contenedor de MariaDB).

---

### 6. Compartir la Imagen Docker (Opcional)

Si deseas compartir esta imagen con otras personas sin que necesiten compilarla, puedes:

- Subir el archivo `.tar` a tu repositorio o servidor.
- O bien, crear un **Docker Registry Privado** para almacenar la imagen de forma accesible.

---

## Resumen de Pasos

1. **Descargar la imagen Docker** (`rr_nextcloud.tar`) desde el enlace proporcionado.
2. **Cargar la imagen** en tu sistema con el comando `docker load`.
3. **Correr el contenedor** con el comando `docker run`.
4. **(Opcional) Usar Docker Compose** para configurar la imagen automáticamente.
5. **Acceder a Nextcloud** desde tu navegador en `http://localhost:8080`.

---

¡Con estos pasos, tendrás Nextcloud corriendo en tu entorno local usando Docker! 😊

---

## Contacto

Para soporte o sugerencias, no dudes en contactar al desarrollador:

- **Ricardo Rosero**  
  Email: [rrosero2000@gmail.com](mailto:rrosero2000@gmail.com)  
  GitHub: [https://github.com/rr-n4p5t3r](https://github.com/rr-n4p5t3r)
