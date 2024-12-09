# Usamos una imagen base oficial de PHP 8.1 con Apache
FROM php:8.1-apache

# Información del desarrollador
LABEL maintainer="Ricardo Rosero <rrosero2000@gmail.com>"
LABEL version="1.0"
LABEL description="Imagen Docker para Nextcloud, desarrollada por Ricardo Rosero"
LABEL repository="https://github.com/rr-n4p5t3r"

# Instalar dependencias necesarias para extensiones de PHP
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libzip-dev \
    libonig-dev \
    libicu-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    unzip \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) \
        gd \
        mysqli \
        pdo_mysql \
        curl \
        mbstring \
        intl \
        xml \
        zip \
        bcmath \
    && rm -rf /var/lib/apt/lists/*

# Habilitar módulos de Apache necesarios para Nextcloud
RUN a2enmod rewrite headers ssl \
    && echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Descargar y extraer Nextcloud
WORKDIR /var/www/html
RUN curl -sSL https://download.nextcloud.com/server/releases/nextcloud-29.0.10.zip -o nextcloud.zip \
    && unzip nextcloud.zip \
    && rm nextcloud.zip

# Cambiar permisos para el directorio de Nextcloud
RUN chown -R www-data:www-data /var/www/html/nextcloud

# Copiar configuración personalizada de Apache
COPY apache-config.conf /etc/apache2/sites-available/000-default.conf

# Exponer el puerto 80
EXPOSE 80

# Comando para iniciar Apache en primer plano
CMD ["apache2-foreground"]
