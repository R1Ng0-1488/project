# project

## Запуск проекта

### установите docker и docker-compose, инструкция по установке [docker](https://docs.docker.com/engine/install/), [docker-compose](https://docs.docker.com/compose/install/)

### запуск проекта: docker-compose up
### создание миграций: docker-compose exec web python manage.py makemigrations
### выполнение миграций: docker-compose exec web python manage.py migrate
### создание суперюзера: docker-compose exec web python manage.py createsuperuser