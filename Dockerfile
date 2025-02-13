FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY reqariments.txt reqariments.txt

RUN pip install --upgrade pip
RUN pip install -r reqariments.txt

COPY FoodBook .

CMD ['gunicorn','FoodBook.wsgi:application','--bind', "0.0.0.0:8000" ]