FROM python:3.7.2-alpine3.9
LABEL MAINTAINER developer_name

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9000

ENV NAME Hello from Dockerfile

ENV BGCOLOR blue

CMD ["python","app.py"]
