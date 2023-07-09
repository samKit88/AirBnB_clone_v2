#!/usr/bin/env bash
# sets up the webs servers for the deployment of web_static

# installs nginx if not already installed
if ! dpkg -s nginx > /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

echo '<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            text-align: center;
        }
    </style>
</head>

<body>
    <h1>TEST PAGE</h1>
</body>

</html>

' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
text='\\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n'
sed -i "24i $text" /etc/nginx/sites-enabled/default
sudo service nginx restart