#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/azizyarzai/DSM.git'

PROJECT_BASE_PATH='/usr/local/apps/dsm'

echo "Installing dependencies..."
apt-get update
apt-get install -y python3-dev python3-venv python3-pip supervisor nginx git python-psycopg2

# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env
source $PROJECT_BASE_PATH/env/bin/activate

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip3 install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip3 install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python3 dsm/manage.py migrate
$PROJECT_BASE_PATH/env/bin/python3 dsm/manage.py collectstatic --noinput

# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_dsm.conf /etc/supervisor/conf.d/dsm.conf
supervisorctl reread
supervisorctl update
supervisorctl restart dsm

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_dsm.conf /etc/nginx/sites-available/dsm.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/dsm.conf /etc/nginx/sites-enabled/dsm.conf
systemctl restart nginx.service

echo "DONE! :)"
