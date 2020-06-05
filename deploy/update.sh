#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/dsm'

git pull
$PROJECT_BASE_PATH/env/bin/python3 src/manage.py makemigrations
$PROJECT_BASE_PATH/env/bin/python3 src/manage.py migrate
$PROJECT_BASE_PATH/env/bin/python3 src/manage.py collectstatic --noinput
supervisorctl restart dsm

echo "DONE! :)"
