FROM python:3.8.3-slim
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY ping-pong.py /
EXPOSE 8080/tcp
CMD [ "python", "./ping-pong.py" ]
