FROM python:2.7-slim
LABEL MAINTAINER developer_name

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 9000

ENV NAME Hello from Dockerfile

ENV BGCOLOR blue

CMD ["python","app.py"]
