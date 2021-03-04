# Family budgets

## Requirements

- docker
- docker-compose
- make

## Setup app

```shell
# Build app, apply migrations and collect static
make build-all
# Run app
make
# Show logs
make logs
```

## All commands

```shell
run:                    Run application
stop:                   Stop application
build:                  Build application
build-all:              Fresh build, apply migration, collect static, load fixtures
test:                   Run tests
purge:                  Clean up
logs:                   Display logs
cli:                    Open command line
shell:                  Open django shell
collectstatic:          Collect static files
migrate:                Migrate database (optional param: app=app_name)
makemigrations:         Make new migrations (optional param: app=app_name)
startapp:               Create a new app required param: app=app_name
dumpdata:               Dump database to file
loaddata:               Load database from file
help:                   Show this help.
```

## Fixtures credentials

* **Login**
  root
* **Password**
  root

## Postman collection

[link](Family%20Budgets.postman_collection.json)
