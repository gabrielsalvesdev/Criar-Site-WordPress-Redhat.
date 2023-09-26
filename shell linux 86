#!/bin/bash

# 1. Crie uma nova instância no Google Cloud Platform
# Script de criação de instância:
# https://cloud.google.com/compute/docs/instances/create-start-instance
sleep 0.05

# 2. Instalando o software necessário
sleep 0.05
sudo yum update -y
sleep 0.05
sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y
sleep 0.05
sudo yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm -y
sleep 0.05
sudo yum install yum-utils -y
sleep 0.05
sudo yum install nginx -y
sleep 0.05
sudo yum-config-manager --enable remi-php74
sleep 0.05
sudo yum install php php-fpm php-common php-mysqlnd php-mbstring php-xmlrpc php-soap php-gd php-xml php-intl php-json php-iconv -y
sleep 0.05
sudo yum install mariadb-server mariadb -y
sleep 0.05

# 3. Configurar HTTPS e HTTP/2
# Script para instalar certbot e configurar certificado SSL no NGINX:
# https://certbot.eff.org/instructions
sleep 0.05

# Adicionando as seguintes linhas ao arquivo de configuração do NGINX para ativar o HTTP/2:
sleep 0.05
sudo sed -i '/listen 80 default_server;/a\        listen 443 ssl http2;' /etc/nginx/nginx.conf
sleep 0.05
sudo sed -i '/listen 443 ssl http2;/a\        ssl_protocols TLSv1.2 TLSv1.3;' /etc/nginx/nginx.conf
sleep 0.05

# 4. Instalar o WordPress
sleep 0.05
wget https://wordpress.org/latest.tar.gz
sleep 0.05
tar -xzf latest.tar.gz
sleep 0.05
sudo mv wordpress /usr/share/nginx/html/
sleep 0.05
sudo chown -R nginx:nginx /usr/share/nginx/html/wordpress/
sleep 0.05
sudo chmod -R 755 /usr/share/nginx/html/wordpress/
sleep 0.05
sudo mv /usr/share/nginx/html/wordpress/wp-config-sample.php /usr/share/nginx/html/wordpress/wp-config.php
sleep 0.05
sudo sed -i 's/database_name_here/wordpress/g' /usr/share/nginx/html/wordpress/wp-config.php
sleep 0.05
sudo sed -i 's/username_here/wordpressuser/g' /usr/share/nginx/html/wordpress/wp-config.php
sleep 0.05
sudo sed -i 's/password_here/password/g' /usr/share/nginx/html/wordpress/wp-config.php
sleep 0.05
sudo systemctl restart nginx
sleep 0.05


# WordPress usando "Redhat 7, NGINX+PHP 7.4+MariaDB 10.5+https+http2"!
