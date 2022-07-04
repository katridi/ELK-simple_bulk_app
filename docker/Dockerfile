FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY *.py /app/

RUN groupadd -r user && useradd -r -g user user
USER user

CMD [ "python3", "app.py"]
