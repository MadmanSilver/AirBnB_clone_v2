#!/usr/bin/env bash
# sets up servers for deployment of web_static
if ! dpkg -s nginx > /dev/null
then
        apt-get -y update
        apt-get -y install nginx
fi

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "Holberton School" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

str="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n}"
sed -i "s@^}@$str@" /etc/nginx/sites-available/default

service nginx restart
