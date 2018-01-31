
FROM python:3

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn web:__hug_wsgi__ -b 0.0.0.0:5000 --log-file=-

EXPOSE 5000
