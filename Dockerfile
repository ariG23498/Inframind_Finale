FROM ubuntu:16.04

RUN apt-get update -y && \
    add-apt-repository ppa:jonathonf/python-3.6 \
    apt-get update \
    apt-get install python3.6

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
