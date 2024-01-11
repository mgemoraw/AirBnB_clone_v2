#!/usr/bin/env bash
# Bash script that sets up my webservers for the deployment of web_static

sudo apt-get update -y
sudo apt-get -y upgrade
# install nginx if not installed
sudo apt-get install -y nginx

# creating directories and files
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create index.html and set text to 'Hello mgemoraw!'
sudo echo "
    <!DOCTYPE HTML>
    <html>
        <head>
            <title>home</title>
        </head>
        <body>
            <h1>Hello mgemoraw! </h1>
        </body>
    </html>" | sudo tee /data/web_static/releases/test/index.html

# creating symbolic link to /data/web_static/current with -sf option
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving owenership of the /data/ folder to the ubuntu and user
sudo chown -hR ubuntu:ubuntu /data/

#update Nginx configuration to serve the conent of 
# /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart service
sudo service nginx start
