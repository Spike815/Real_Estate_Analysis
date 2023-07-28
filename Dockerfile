FROM ubuntu
FROM python:3.11


WORKDIR /code

COPY ./deployment_requirements.txt /code/deployment_requirements.txt 

RUN pip install --no-cache-dir --upgrade -r deployment_requirements.txt

COPY ./src /code/src
COPY ./app.py /code/app.py

CMD ["uvicorn", "app:app","--host", "0.0.0.0", "--port", "80"]