FROM python:3.10.12-alpine3.18

WORKDIR /consumer

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apk update

COPY ./requirements.txt /consumer/requirements.txt

RUN pip install -r requirements.txt

COPY ./consumer/ /consumer/

CMD [ "executable" ]