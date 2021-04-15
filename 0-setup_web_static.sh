#!/usr/bin/env bash
# Bash script to setup a web server for the deployement of web_static.

# Install Nginx if not already installed
apt update -y >/dev/null 2>&1
apt install nginx -y >/dev/null 2>&1

# Create required directories if they don't exist
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create fake index.html file
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" >/data/web_static/releases/test/index.html

# Create the symbolic link
ln -snf /data/web_static/releases/test /data/web_static/current

# Change ownership of files and folders inside of /data folder
chown -R ubuntu:ubuntu /data

# Add alias to serve the content of /data/web_static/current to hbnb_static
if ! grep -q 'location \/hbnb_static\/' /etc/nginx/sites-available/default; then
	sed -i '/server_name _;/a\\n        location /hbnb_static/ {\n                alias /data/web_static/current/;\n        }' /etc/nginx/sites-available/default
fi

# Restart the nginx service
service nginx restart
