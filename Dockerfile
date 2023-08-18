FROM python:3.8
RUN apt-get update -y

WORKDIR /var/app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . /var/app

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "8071"]