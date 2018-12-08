run:
	python rentsite/manage.py runserver

migrate:
	python rentsite/manage.py migrate

makemigraions:
	python rentsite/manage.py makemigrations

shell:
	python rentsite/manage.py shell

all:
	python rentsite/manage.py makemigrations
	python rentsite/manage.py migrate
	python rentsite/manage.py runserver
