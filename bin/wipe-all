#!/usr/bin/env bash

if ! ls | grep bin >/dev/null; then
    cd ..
    if ! ls | grep bin >/dev/null; then
        echo 'Please run in project root directory!'
        exit 1
    fi
fi

echo '┌——————————————————————————————————┐'
echo '|  WARNING: THIS WILL WIPE THE DB  |'
echo '└——————————————————————————————————┘'

if [[ "$response" != 'force' ]]; then
    read -r -p '⚠️  Are you SURE? [y/N] ' response
    if [[ "$response" != 'y' && "$response" != 'Y' ]]; then
        exit
    fi
fi

if [[ -z "$(docker ps -aq -f name=mysql 2>/dev/null)" ]]; then
    echo 'Running mysql-cmdline container'
    docker run --name mysql-cmdline --link mysql:db mysql:5.7.14
elif [[ -z "$(docker ps -aq -f name=mysql -f status=running 2>/dev/null)" ]]; then
    echo 'Starting mysql-cmdline container'
    docker start mysql-cmdline >/dev/null
else
    echo 'Skipping mysql-cmdline initialization'
fi

echo 'Recreating database'
query="DROP DATABASE IF EXISTS cs4501;create database cs4501 character set utf8;grant all on cs4501.* to 'www'@'%';"
docker exec -it mysql-cmdline bash -c "mysql -uroot -p'\$3cureUS' -h db -e '$query'"

echo 'Wiping old migrations'
rm -f market/project2/migrations/*_initial.py

unset response
