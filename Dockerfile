FROM python:latest

COPY main.py /main.py

CMD [ "python3", "main.py"]