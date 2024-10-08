FROM python:3.11.10-slim
WORKDIR /app/
COPY ./app/ /app/
RUN apt-get update
RUN pip install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]