FROM python:3.9.7-slim
RUN apt-get update && apt-get install gcc -y && apt-get clean
COPY . /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","main:app","--reload","--host","0.0.0.0"]