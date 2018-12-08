run:
	python src/manage.py runserver

migrate:
	python src/manage.py migrate

makemigraions:
	python src/manage.py makemigrations

shell:
	python src/manage.py shell

all:
	python src/manage.py makemigrations
	python src/manage.py migrate
	python src/manage.py runserver
