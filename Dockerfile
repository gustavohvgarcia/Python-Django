FROM python:3.8

WORKDIR /webapp

# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y libsqlite3-dev
RUN pip install -U pip setuptools

COPY requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . .
# Django service
EXPOSE 8000

RUN chmod +x ./run_web.sh
CMD ["./run_web.sh"]
