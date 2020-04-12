.PHONY: all help translate test clean update compass collect rebuild

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: test - calls the "test" django command
test:
	docker-compose run backend python manage.py test

# target: bash
bash:
	docker-compose exec backend bash

# target: test - calls the "test" django command
shell:
	docker-compose run backend python manage.py shell_plus

# target: clean - remove all ".pyc" files
clean:
	docker-compose run backend python manage.py clean_pyc

# target: update - install (and update) pip requirements
update:
	docker-compose run backend pip install -r requirements/dev.txt

# target: collect - calls the "collectstatic" django command
collect:
	docker-compose run backend python manage.py collectstatic --noinput

# target: collect - calls the "makemigrations" django command
migrations:
	docker-compose run backend python manage.py makemigrations

# target: collect - calls the "migrate" django command
migrate:
	docker-compose run backend python manage.py migrate

# target: rebuild - clean, update, collect, then rebuild all data
rebuild: clean update collect
	docker-compose run backend python manage.py reset_db --noinput
	docker-compose run backend python manage.py makemigrations
	docker-compose run backend python manage.py migrate

# Builds the frontend
build:
	rm -rf frontend/dist/*
	docker-compose run frontend yarn build
