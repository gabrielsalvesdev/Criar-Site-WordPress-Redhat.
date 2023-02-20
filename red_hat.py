import os
import subprocess

# 1. Crie uma nova instância no Google Cloud Platform
# Script de criação de instância:
# https://cloud.google.com/compute/docs/instances/create-start-instance
time.sleep(0.05)

# 2. Instale o software necessário
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'update', '-y'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'install', 'epel-release', '-y'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'install', 'http://rpms.remirepo.net/enterprise/remi-release-7.rpm', '-y'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'install', 'yum-utils', '-y'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'install', 'nginx', '-y'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum-config-manager', '--enable', 'remi-php74'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'install', 'php', 'php-fpm', 'php-common', 'php-mysqlnd', 'php-mbstring', 'php-xmlrpc', 'php-soap', 'php-gd', 'php-xml', 'php-intl', 'php-json', 'php-iconv', '-y'])
time.sleep(0.05)
subprocess.call(['sudo', 'yum', 'install', 'mariadb-server', 'mariadb', '-y'])
time.sleep(0.05)

# 3. Configure HTTPS e HTTP/2
# Script para instalar certbot e configurar certificado SSL no NGINX:
# https://certbot.eff.org/instructions
time.sleep(0.05)

# Adicione as seguintes linhas ao arquivo de configuração do NGINX para ativar o HTTP/2:
time.sleep(0.05)
os.system("sudo sed -i '/listen 80 default_server;/a\        listen 443 ssl http2;' /etc/nginx/nginx.conf")
time.sleep(0.05)
os.system("sudo sed -i '/listen 443 ssl http2;/a\        ssl_protocols TLSv1.2 TLSv1.3;' /etc/nginx/nginx.conf")
time.sleep(0.05)

# 4. Instale o WordPress
time.sleep(0.05)
os.system("wget https://wordpress.org/latest.tar.gz")
time.sleep(0.05)
os.system("tar -xzf latest.tar.gz")
time.sleep(0.05)
os.system("sudo mv wordpress /usr/share/nginx/html/")
time.sleep(0.05)
os.system("sudo chown -R nginx:nginx /usr/share/nginx/html/wordpress/")
time.sleep(0.05)
os.system("sudo chmod -R 755 /usr/share/nginx/html/wordpress/")
time.sleep(0.05)
os.system("sudo mv /usr/share/nginx/html/wordpress/wp-config-sample.php /usr/share/nginx/html/wordpress/wp-config.php")
time.sleep(0.05)
os.system("sudo sed -i 's/database_name_here/wordpress/g' /usr/share/nginx/html/wordpress/wp-config.php")
time.sleep(0.05)
os.system("sudo sed -i 's/username_here/wordpressuser/g' /usr/share/nginx/html/wordpress/wp-config.php")
time.sleep(0.05)
os.system("sudo sed -i 's/password_here/password/g' /usr
