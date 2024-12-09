## Uso de la imagen Docker de Nextcloud

Esta imagen Docker está diseñada para ser utilizada en el entorno de desarrollo de Nextcloud. Ha sido desarrollada por Ricardo Rosero.

### Cargar la imagen

1. Primero, descarga el archivo `rr_nextcloud.tar` desde la carpeta `docker_images/`.

2. Luego, carga la imagen Docker en tu sistema local:

   ```bash
   docker load -i docker_images/rr_nextcloud.tar

3. Una vez cargada, puedes correr el contenedor utilizando:

    ```bash
   docker run -d -p 8080:80 nextcloud:latest


---

### **Compartir la imagen (Opcional)**
Si deseas que otras personas puedan descargar la imagen desde tu repositorio sin necesidad de compilarla, también puedes crear un **docker registry privado** y subir la imagen allí, o bien compartir el archivo `.tar` directamente.

---

### **Resumen de pasos:**

1. **Guardar la imagen Docker** con `docker save`.
2. **Mover el archivo `.tar`** a tu repositorio o proyecto.
3. **Documentar tu imagen Docker** dentro del `Dockerfile` usando la instrucción `LABEL`.
4. **Subir el archivo `.tar`** al repositorio (opcional).
5. **Incluir instrucciones en el README** para que otros usen la imagen.
6. (Opcional) Crear un **docker registry privado** para compartir la imagen.

---

¡Con estos pasos, tu imagen estará documentada y disponible para otros usuarios de tu proyecto! 😊
