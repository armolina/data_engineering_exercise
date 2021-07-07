FROM python:3.8-slim

COPY . /home/app
COPY ./origin_data/core /tmp

WORKDIR /home/app

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

CMD [ "python3.8", "-u", "app.py" ]