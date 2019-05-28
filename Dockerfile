FROM python:3.6

MAINTAINER AnaPaula

ADD /404-portal /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -U pip

RUN pip install --no-cache-dir -r requeriments.txt

EXPOSE 8000

CMD exec gunicorn portal.wsgi:application --bind 0.0.0.0:8000 --workers 3
