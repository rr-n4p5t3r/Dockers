#!/bin/bash
# Script para instalar Docker en Linux Mint 22+

# Actualizar el sistema
sudo apt update
sudo apt upgrade -y

# Instalar dependencias necesarias
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Agregar la clave GPG oficial de Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Agregar el repositorio de Docker
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Actualizar la lista de paquetes y instalar Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io -y

# Verificar que Docker esté instalado correctamente
sudo docker --version

# Agregar el usuario actual al grupo de Docker (para evitar usar sudo)
sudo usermod -aG docker $USER

echo "Instalación de Docker completada. Reinicia el sistema o vuelve a iniciar sesión para aplicar los cambios."
