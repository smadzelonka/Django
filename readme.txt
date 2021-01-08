1.
python3 -m venv .env
2.
source .env/bin/activate
3.
pip3 install django
4.
pip3 install psycopg2
5.
pip3 freeze > requirements.txt
6.
django-admin startproject catcollector_project . 
7.
python3 manage.py startapp main_app
8.
python manage.py runserver
9.
Add your server in settings and createdb 
10.
python manage.py migrate

================Git pull down =============
1.
python3 -m venv .env
2.
source .env/bin/activate
3.
pip3 install -r requirements.txt
4.
python manage.py runserver
5.
add server db
6.
python manage.py migrate




=========
python manage.py makemigrations