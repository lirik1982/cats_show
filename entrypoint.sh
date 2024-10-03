#!/bin/sh

python manage.py migrate

python manage.py loaddata fixtures/user.json
python manage.py loaddata fixtures/catbreed.json
python manage.py loaddata fixtures/cats.json
python manage.py loaddata fixtures/rating.json

python manage.py runserver 0.0.0.0:8000


