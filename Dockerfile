# https://github.com/thomaspinckney3/django-docker.git

FROM grahamdumpleton/mod-wsgi-docker:python-3.5

RUN apt-get update && \
            apt-get install -y --no-install-recommends git \
            python-pip \
            python-dev \
            libmysqlclient-dev \
	    unattended-upgrades && \
            rm -r /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install \
    "django==1.10" \
	"mysqlclient==1.3.8" \
	"kafka-python<=1.0" \
	"elasticsearch<3.0" \
	"djangorestframework==3.6.4" \
	"requests==2.18.4" \
	"libsass==0.13.2" \
	"django-compressor==2.2" \
	"django-sass-processor==0.5.5"

ENV LANG=en_US.UTF-8 PYTHONHASHSEED=random \
    PATH=/usr/local/python/bin:/usr/local/apache/bin:$PATH \
    MOD_WSGI_USER=www-data MOD_WSGI_GROUP=www-data

WORKDIR /app

# Switching from mysql-connector to mysqlclient requires that
# the database engine be changed from 'ENGINE': 'mysql.connector.django' to
# 'ENGINE': 'django.db.backends.mysql'
