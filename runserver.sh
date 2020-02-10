#!/usr/bin/env sh
if [ ${1} != "dev" ] && [ ${1} != "prod" ];
  then echo "use 'dev' or 'prod' for parameter."
else
  sh -ac "source ./envs/${1}.env && python manage.py runserver_plus"
fi
