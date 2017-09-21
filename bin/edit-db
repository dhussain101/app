#!/usr/bin/env bash

if [[ -z "$(docker ps -aq -f name=mysql 2>/dev/null)" ]]; then
    echo 'Running mysql-cmdline container'
    docker run --name mysql-cmdline --link mysql:db mysql:5.7.14
elif [[ -z "$(docker ps -aq -f name=mysql -f status=running 2>/dev/null)" ]]; then
    echo 'Starting mysql-cmdline container'
    docker start mysql-cmdline >/dev/null
else
    echo 'Skipping mysql-cmdline initialization'
fi

echo 'Entering mysql repl'
echo
docker exec -it mysql-cmdline bash -c "mysql -uroot -p'\$3cureUS' -h db cs4501"
