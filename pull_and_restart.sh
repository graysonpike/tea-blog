cd /home/grayson/tea-blog/
source env/bin/activate
git pull
cd teablog
python manage.py migrate
python manage.py collectstatic
sudo systemctl restart gunicorn-tea-blog
