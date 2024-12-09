import docker
import subprocess

# Crear cliente Docker
client = docker.from_env()

def listar_contenedores():
    """Lista los contenedores en ejecución."""
    try:
        # Crear el cliente de Docker
        client = docker.from_env()

        # Obtener los contenedores activos
        containers = client.containers.list()

        if not containers:
            print("No hay contenedores en ejecución.")
            return

        for container in containers:
            print(f"Contenedor ID: {container.id}")
            print(f"Nombre: {container.name}")
            print(f"Estado: {container.status}")
            print("-" * 30)

    except docker.errors.DockerException as e:
        print(f"Error al conectar con Docker: {e}")

def listar_imagenes():
    """Lista las imágenes locales."""
    images = client.images.list()  # Obtener las imágenes locales
    if not images:
        print("No hay imágenes locales.")
        return

    for image in images:
        print(f"Imagen ID: {image.id}")
        print(f"Etiquetas: {image.tags}")
        print("-" * 30)

if __name__ == "__main__":
    print("Contenedores en ejecución:")
    listar_contenedores()
    print("\nImágenes locales:")
    listar_imagenes()
