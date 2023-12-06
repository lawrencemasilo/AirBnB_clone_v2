#!/usr/bin/env bash
#sets up web servers for the deployment of web_static

if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

nginx_config="server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
    }
}"

echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo service nginx restart

exit 0
