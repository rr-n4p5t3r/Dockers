
# DockerDesktop

DockerDesktop es una aplicación desarrollada en Python diseñada para gestionar contenedores Docker de manera sencilla y eficiente. Es especialmente útil para sistemas operativos no compatibles con la aplicación oficial de Docker Desktop.

---

## **Propósito**

Esta aplicación permite a los usuarios:
- Visualizar contenedores Docker en ejecución.
- Administrar imágenes, volúmenes y redes de Docker.
- Realizar tareas comunes como iniciar, detener y eliminar contenedores.
  
DockerDesktop proporciona una alternativa ligera y funcional para usuarios cuyo sistema operativo no admite la app oficial Docker Desktop.

---

## **Requisitos previos**

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Docker y Docker Compose
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar este repositorio)

---

## **Instrucciones de instalación**

### 1. Clonar el repositorio (opcional)
Si tienes Git instalado, puedes clonar este repositorio con:
```bash
git clone https://github.com/tu-usuario/dockerdesktop.git
cd dockerdesktop
```
Si no tienes Git, descarga el archivo ZIP del proyecto desde [aquí](https://github.com/tu-usuario/dockerdesktop) y descomprímelo.

---

### 2. Crear un entorno virtual
En el directorio del proyecto, ejecuta los siguientes comandos:

#### En Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependencias
Con el entorno virtual activado, instala las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4. Configuración previa
Asegúrate de que Docker esté instalado y en ejecución en tu sistema. Verifica que tienes los permisos necesarios para ejecutar comandos de Docker.

Para verificar la instalación de Docker, puedes ejecutar:
```bash
docker --version
docker-compose --version
```

---

### 5. Ejecutar la aplicación
Ejecuta el archivo `app.py` para iniciar DockerDesktop:

```bash
python app.py
```

---

## **Estructura del proyecto**

```
dockerdesktop/
├── app.py                # Archivo principal de la aplicación
├── requirements.txt      # Dependencias necesarias para ejecutar la aplicación
├── README.md             # Este archivo
└── ...
```

---

## **Características**

- Gestión de contenedores Docker: iniciar, detener y eliminar.
- Exploración de imágenes, volúmenes y redes de Docker.
- Interfaz amigable para sistemas no compatibles con Docker Desktop.

---

## **Notas**

1. Si encuentras algún problema con las dependencias, asegúrate de estar en el entorno virtual y de usar la versión recomendada de Python.
2. Verifica que Docker esté correctamente configurado en tu sistema.
3. Si necesitas más ayuda, no dudes en contactarme a través de [mi correo](mailto:rrosero2000@gmail.com).

---

¡Gracias por usar DockerDesktop! 😊