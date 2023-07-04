FROM python:3.11.4-alpine3.18

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apk update

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./app/ /app/

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload" ]