import subprocess
import json  # Asegúrate de importar json
import re
from flask import Flask, render_template, request, redirect
import docker

# Crear cliente Docker
docker_client = docker.from_env()

app = Flask(__name__)

# Obtener contenedores
def get_containers():
    containers = []
    for container in docker_client.containers.list(all=True):  # Obtiene todos los contenedores
        containers.append({
            'Names': container.name,  # Devuelve el nombre completo del contenedor
            'ID': container.id,
            'Image': container.image.tags[0] if container.image.tags else 'Sin etiqueta',  # Imagen asociada
            'Status': container.status,  # Estado del contenedor (ej. "running", "exited")
        })
    return containers


# Obtener imágenes
def get_images():
    result = subprocess.run(['docker', 'images', '--format', '{{.Repository}} {{.Tag}} {{.ID}} {{.CreatedSince}} {{.Size}}'], capture_output=True, text=True)

    images = []
    for line in result.stdout.splitlines():
        repo, tag, image_id, created_since, size = line.split(maxsplit=4)

        # Manejar imágenes sin etiqueta
        if tag == '<none>':
            tag = 'Sin etiqueta'

        # Eliminar texto adicional de "hours ago", "days ago", etc. y convertir el tamaño a número
        size_value = 0.0
        # Usamos expresiones regulares para extraer el valor numérico y la unidad
        match = re.search(r'(\d+(\.\d+)?)\s*(GB|MB|KB)?', size.strip())
        if match:
            number = float(match.group(1))
            unit = match.group(3)

            # Convertir según la unidad
            if unit == 'GB':
                size_value = number * 1024  # Convertir GB a MB
            elif unit == 'MB':
                size_value = number
            elif unit == 'KB':
                size_value = number / 1024  # Convertir KB a MB
            else:
                size_value = number  # Sin unidad, asumimos MB por defecto

        images.append({
            'Repository': repo,
            'Tag': tag,
            'ImageID': image_id,
            'CreatedSince': created_since,
            'Size': size_value
        })

    return images

@app.route('/')
def index():
    containers = get_containers()
    images = get_images()
    return render_template('index.html', containers=containers, images=images)

@app.route('/control/<container_name>', methods=['POST'])
def control_container(container_name):
    action = request.form.get('action')

    if action == 'start':
        subprocess.run(['docker', 'start', container_name])
    elif action == 'stop':
        subprocess.run(['docker', 'stop', container_name])
    elif action == 'restart':
        subprocess.run(['docker', 'restart', container_name])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
