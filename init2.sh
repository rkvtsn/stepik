sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx stop
sudo /usr/sbin/nginx -c /etc/nginx/sites-enabled/test.conf