
FROM python:3

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV PORT 80

CMD gunicorn web:__hug_wsgi__ -b 0.0.0.0:80 --log-file=-

EXPOSE 80
