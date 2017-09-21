#!/usr/bin/env bash

# Search for Dockerfile...
if ! ls | grep Dockerfile >/dev/null; then
    cd ..
    if ! ls | grep Dockerfile>/dev/null; then
        echo 'Please run from the project'"'"'s root directory!'
        echo '🚫  Cannot find Dockerfile, aborting'
        exit 1
    fi
fi

# And search for docker-compose.yml
if ! ls | grep docker-compose.yml>/dev/null; then
    echo '🚫  Cannot find docker-compose.yml, aborting'
    exit 1
fi

# Check if mysql has been run before
if [[ -z "$(docker ps -aq -f name=mysql 2>/dev/null)" ]]; then
    # Check if mysql:5.7.14 is present
    if [[ -z "$(docker images -q mysql:5.7.14 2>/dev/null)" ]]; then
        echo '🌐  Downloading mysql:5.7.14'
        docker pull mysql:5.7.14
    fi
    read -r -p '🤔  Where is your db located? [~/cs4501/db] ' db_dir
    echo
    if [[ -z "$db_dir" ]]; then
        echo '⚠️  Using default directory: ~/cs4501/db'
        db_dir='~/cs4501/db'
    fi
    # Run mysql
    echo '🚀  Running mysql container'
    docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='$3cureUS' -v "$db_dir":/var/lib/mysql  mysql:5.7.14
    response='force'
    ./bin/wipe-all.sh
# Check if mysql is running
elif [[ -z "$(docker ps -aq -f name=mysql -f status=running 2>/dev/null)" ]]; then
    # Ran before, but not currently running
    echo '🚀  Starting mysql container'
    docker start mysql >/dev/null 2>&1
else
    echo '👍  mysql already running'
fi
echo

# Check if custom container has not been built before
if [[ -z "$(docker images -q djangorest 2>/dev/null)" ]]; then
    response='y'
# Check if custom container is running
elif [[ -n "$(docker ps -q -f name=djangorest -f status=running 2>/dev/null)" ]]; then
    echo '⚠️  It looks like you'"'"'re already running the djangorest container.'
    read -r -p 'Would you like to stop djangorest? [y/N] ' response
    if [[ "$response" == 'y' || "$response" == 'Y' ]]; then
        docker-compose down
        read -r -p 'Rebuild? [y/N] ' response
    fi
    if [[ "$response" != 'y' && "$response" != 'Y' ]]; then
        unset response
        exit
    fi
else
    echo '🤔  Rebuild djangorest container? This should be done anytime Dockerfile has been changed. (reply '"'y'"' if unsure)'
    read -r -p '[y/N] ' response
fi

echo

# Build custom container
if [[ "$response" == 'y' || "$response" == 'Y' ]]; then
    # TODO: add versioning?
    echo '🛠  Building djangorest'
    echo '—————————————————————————————————————————————'
    docker build -t djangorest .
else
    echo '⏩  No problem, skipping build'
fi

# Container is not running yet, so start it
echo
echo '⚓️  Composing'
echo '—————————————————————————————————————————————'
docker-compose up

unset response
