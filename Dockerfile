FROM python:3.9 

COPY main.py /main.py

CMD [ "python", "/main.py"]