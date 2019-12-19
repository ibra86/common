FROM python:3.7

RUN pip install django
COPY ./pokemon /app/pokemon
COPY ./manage.py /app

WORKDIR /app

#RUN ls -la #hack

EXPOSE 8000

RUN python manage.py runserver 0:8000