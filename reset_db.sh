#!/bin/bash

FILE="db.sqlite3"

if test -f "$FILE"
then
    echo Database is drop
    rm $FILE
else
    echo Database not exists.
fi

python manage.py makemigrations

python manage.py migrate

python manage.py init
