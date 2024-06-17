python -m venv myvenv
myvenc\Scripts\activate
pip install django
django-admin startproject mysite .
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser  ///set userid and password
Admin User ID : akshay8281
		Password : test@123
python manage.py runserver
python manage.py startapp myapp