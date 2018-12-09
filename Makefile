run:
	python manage.py runserver

migrate:
	python manage.py migrate

makemigraions:
	python manage.py makemigrations

shell:
	python manage.py shell

all:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

install:
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
