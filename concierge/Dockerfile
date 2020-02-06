FROM python:3.8

#RUN ls -la

RUN pip install django
RUN pip install psycopg2
RUN pip install django-redis

COPY . /app

WORKDIR /app

RUN ls -la

EXPOSE 8000

#ENTRYPOINT ["/bin/bash"]
#CMD python manage.py runserver 0:8000
CMD ["python", "manage.py", "runserver", "0:8000"]

#docker build -t my_app .
#docker run --name my_app -d -p 8000:8000 my_app
#docker exec -it my_app bash

#docker run -it --entrypoint /bin/bash my_app