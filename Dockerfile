FROM python:3.12.1-bookworm

RUN mkdir -p /home/app
RUN cd /home/app

COPY equations.py /home/app
COPY rest_api.py /home/app

RUN pip3 install bottle
WORKDIR /home/app
CMD ["python3", "rest_api.py"]