FROM python:3.8.2-alpine

COPY ./web-app /app
WORKDIR /app
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["python3", "server.py"]