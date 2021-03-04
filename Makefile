.PHONY: run stop build rebuild test purge logs cli shell collectstatic migrate makemigrations startapp dumpdata help

run:							## Run application
	docker-compose up -d

stop:							## Stop application
	docker-compose down

build:							## Build application
	docker-compose build

build-all: purge build migrate collectstatic loaddata	## Fresh build, apply migration, collect static, load fixtures

test:							## Run tests
	docker-compose run --rm web python manage.py test

purge:							## Clean up
	docker-compose down --remove-orphans --rmi local -v

logs:							## Display logs
	docker-compose logs -ft --tail 50

cli:							## Open command line
	docker-compose run --rm web sh

shell:							## Open django shell
	docker-compose run --rm web python manage.py shell

collectstatic:						## Collect static files
	docker-compose run --rm web python manage.py collectstatic --no-input --clear

migrate:						## Migrate database (optional param: app=app_name)
	docker-compose run --rm web python manage.py migrate $(value $1)

makemigrations:						## Make new migrations (optional param: app=app_name)
	docker-compose run --rm web python manage.py makemigrations $(app)

startapp:						## Create a new app required param: app=app_name
	docker-compose run --rm web python manage.py startapp "$${app:?param app is required}"

dumpdata:						## Dump database to file
	docker-compose run --rm web python manage.py dumpdata -e contenttypes -e admin.logentry -e sessions -e authtoken --indent 4 > fixtures/initial_data.json

loaddata:						## Load database from file
	docker-compose run --rm web python manage.py loaddata fixtures/*

help:							## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
