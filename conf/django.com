# Default server configuration
#
server {
    listen 80 default_server;
    server_name _;

    access_log  /tmp/bokeh.access.log;
    error_log   /tmp/bokeh.error.log debug;

    location / {
        proxy_pass http://192.168.199.13:8000;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_http_version 1.1;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host:$server_port;
        proxy_buffering off;
    }

}



