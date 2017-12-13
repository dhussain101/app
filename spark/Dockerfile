FROM gettyimages/spark

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		libmysqlclient-dev \
		build-essential \
		unattended-upgrades && \
	rm -r /var/lib/apt/lists/*

RUN apt-get update && \
	apt-get install -y --no-install-recommends \
		python3-dev \
    	python-pip \
    	python-mysqldb && \
	rm -r /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install mysqlclient
