#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static.
if ! [ "$(command -v nginx)" ]; then
	sudo apt-get update
	sudo apt-get install nginx
fi
if [ ! -d "/data/web_static/" ]; then
	sudo mkdir -p /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ]; then
	sudo mkdir -p /data/web_static/releases/
fi
if [ ! -d "/data/web_static/releases/test" ]; then
	sudo mkdir -p /data/web_static/releases/test/
fi
if [ ! -d "/data/web_static/shared/" ]; then
	sudo mkdir -p /data/web_static/shared/
fi
if [ -L /data/web_static/current ]; then
	sudo rm /data/web_static/current
else
	ln -sf /data/web_static/releases/test /data/web_static/current
fi
echo "<html>
  	<head>
  	</head>
  	  <body>
    	    Holberton School
  	  </body>
	</html>" | sudo tee /data/web_static/releases/test/index.html
sudo chown -R "$USER":"$USER" /data/
sudo sed -i 's|root /var/www/html;|root /data/web_static/current;|g' /etc/nginx/sites-available/default
sudo sed -i 's|index index.html index.htm;|index index.html;|g' /etc/nginx/sites-available/default
sudo sed -i 's|server_name _;|server_name mydomainname.tech;|g' /etc/nginx/sites-available/default
sudo sed -i 's|location / {|location /hbnb_static {|g' /etc/nginx/sites-available/default
sudo sed -i '/server {/a \    location /hbnb_static {\n\t\talias /data/web_static/releases/test;\n\t\tindex index.html;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
