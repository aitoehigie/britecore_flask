FROM python:3.6

MAINTAINER Ehigie (@pystar) Aito "<aitoehigie@gmail.com>"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

#ENV FLASK_APP featurerequests

EXPOSE 8000

WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

#RUN python manage.py create_db

#RUN python manage.py init_db

#ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
EXPOSE 8000

CMD ["gunicorn","-b", "0.0.0.0:8000", "manage:app"]
